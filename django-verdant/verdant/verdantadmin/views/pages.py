from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.template import RequestContext

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required

from treebeard.exceptions import InvalidMoveToDescendant

from verdant.verdantcore.models import Page, PageRevision, get_page_types
from verdant.verdantadmin.edit_handlers import TabbedInterface, ObjectList
from verdant.verdantadmin.forms import SearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def index(request, parent_page_id=None):
    if parent_page_id:
        parent_page = get_object_or_404(Page, id=parent_page_id)
    else:
        parent_page = Page.get_first_root_node()

    pages = parent_page.get_children().prefetch_related('content_type')

    # Get page ordering
    if 'ordering' in request.GET:
        ordering = request.GET['ordering']

        if ordering in ['title', '-title', 'content_type', '-content_type', 'live', '-live']:
            pages = pages.order_by(ordering)
    else:
        ordering = None

    return render(request, 'verdantadmin/pages/index.html', {
        'parent_page': parent_page,
        'ordering': ordering,
        'pages': pages,
    })


@login_required
def select_type(request):
    # Get the list of page types that can be created within the pages that currently exist
    existing_page_types = ContentType.objects.raw("""
        SELECT DISTINCT content_type_id AS id FROM verdantcore_page
    """)

    page_types = set()
    for ct in existing_page_types:
        allowed_subpage_types = ct.model_class().clean_subpage_types()
        for subpage_type in allowed_subpage_types:
            subpage_content_type = ContentType.objects.get_for_model(subpage_type)

            page_types.add(subpage_content_type)

    return render(request, 'verdantadmin/pages/select_type.html', {
        'page_types': page_types,
    })


@login_required
def add_subpage(request, parent_page_id):
    parent_page = get_object_or_404(Page, id=parent_page_id).specific

    page_types = sorted([ContentType.objects.get_for_model(model_class) for model_class in parent_page.clean_subpage_types()], key=lambda pagetype: pagetype.name)
    all_page_types = sorted(get_page_types(), key=lambda pagetype: pagetype.name)

    return render(request, 'verdantadmin/pages/add_subpage.html', {
        'parent_page': parent_page,
        'page_types': page_types,
        'all_page_types': all_page_types,
    })

@login_required
def select_location(request, content_type_app_name, content_type_model_name):
    try:
        content_type = ContentType.objects.get_by_natural_key(content_type_app_name, content_type_model_name)
    except ContentType.DoesNotExist:
        raise Http404

    page_class = content_type.model_class()
    # page_class must be a Page type and not some other random model
    if not issubclass(page_class, Page):
        raise Http404

    # find all the valid locations (parent pages) where a page of the chosen type can be added
    parent_pages = page_class.allowed_parent_pages()

    if len(parent_pages) == 0:
        # user cannot create a page of this type anywhere - fail with an error
        messages.error(request, "Sorry, you do not have access to create a page of type '%s'." % content_type.name)
        return redirect('verdantadmin_pages_select_type')
    elif len(parent_pages) == 1:
        # only one possible location - redirect them straight there
        return redirect('verdantadmin_pages_create', content_type_app_name, content_type_model_name, parent_pages[0].id)
    else:
        # prompt them to select a location
        return render(request, 'verdantadmin/pages/select_location.html', {
            'content_type': content_type,
            'page_class': page_class,
            'parent_pages': parent_pages,
        })


@login_required
def create(request, content_type_app_name, content_type_model_name, parent_page_id):
    parent_page = get_object_or_404(Page, id=parent_page_id).specific

    try:
        content_type = ContentType.objects.get_by_natural_key(content_type_app_name, content_type_model_name)
    except ContentType.DoesNotExist:
        raise Http404

    page_class = content_type.model_class()

    # page must be in the list of allowed subpage types for this parent ID
    # == Restriction temporarily relaxed so that as superusers we can add index pages and things -
    # == TODO: reinstate this for regular editors when we have distinct user types
    #
    # if page_class not in parent_page.clean_subpage_types():
    #     messages.error(request, "Sorry, you do not have access to create a page of type '%s' here." % content_type.name)
    #     return redirect('verdantadmin_pages_select_type')

    page = page_class()
    edit_handler_class = get_page_edit_handler(page_class)
    form_class = edit_handler_class.get_form_class(page_class)

    if request.POST:
        form = form_class(request.POST, request.FILES, instance=page)

        # Stick an extra validator into the form to make sure that the slug is not already in use
        def clean_slug(slug):
            # Make sure the slug isn't already in use
            if parent_page.get_children().filter(slug=slug).count() > 0:
                raise ValidationError("This slug is already in use")
            return slug
        form.fields['slug'].clean = clean_slug

        if form.is_valid():
            page = form.save(commit=False)  # don't save yet, as we need treebeard to assign tree params

            is_publishing = bool(request.POST.get('action-publish')) and request.user.has_perm('core.can_publish_page')
            is_submitting = bool(request.POST.get('action-submit'))

            if is_publishing:
                page.live = True
                page.has_unpublished_changes = False
            else:
                page.live = False
                page.has_unpublished_changes = True

            parent_page.add_child(page)  # assign tree parameters - will cause page to be saved
            page.save_revision(user=request.user, submitted_for_moderation=is_submitting)

            if is_publishing:
                messages.success(request, "Page '%s' published." % page.title)
            elif is_submitting:
                messages.success(request, "Page '%s' submitted for moderation." % page.title)
            else:
                messages.success(request, "Page '%s' created." % page.title)
            return redirect('verdantadmin_explore', page.get_parent().id)
        else:
            messages.error(request, "The page could not be created due to validation errors")
            edit_handler = edit_handler_class(instance=page, form=form)
    else:
        form = form_class(instance=page)
        edit_handler = edit_handler_class(instance=page, form=form)

    return render(request, 'verdantadmin/pages/create.html', {
        'content_type': content_type,
        'page_class': page_class,
        'parent_page': parent_page,
        'edit_handler': edit_handler,
    })


@login_required
def edit(request, page_id):
    latest_revision = get_object_or_404(Page, id=page_id).get_latest_revision()
    page = get_object_or_404(Page, id=page_id).get_latest_revision_as_page()

    edit_handler_class = get_page_edit_handler(page.__class__)
    form_class = edit_handler_class.get_form_class(page.__class__)

    errors_debug = None

    if request.POST:
        form = form_class(request.POST, request.FILES, instance=page)

        if form.is_valid():
            is_publishing = bool(request.POST.get('action-publish')) and request.user.has_perm('core.can_publish_page')
            is_submitting = bool(request.POST.get('action-submit'))

            if is_publishing:
                page.live = True
                page.has_unpublished_changes = False
                form.save()
                page.revisions.update(submitted_for_moderation=False)
            else:
                # not publishing the page
                if page.live:
                    # To avoid overwriting the live version, we only save the page
                    # to the revisions table
                    form.save(commit=False)
                    Page.objects.filter(id=page.id).update(has_unpublished_changes=True)
                else:
                    page.has_unpublished_changes = True
                    form.save()

            page.save_revision(user=request.user, submitted_for_moderation=is_submitting)

            if is_publishing:
                messages.success(request, "Page '%s' published." % page.title)
            elif is_submitting:
                messages.success(request, "Page '%s' submitted for moderation." % page.title)
            else:
                messages.success(request, "Page '%s' updated." % page.title)
            return redirect('verdantadmin_explore', page.get_parent().id)
        else:
            messages.error(request, "The page could not be saved due to validation errors")
            edit_handler = edit_handler_class(instance=page, form=form)
            errors_debug = (
                repr(edit_handler.form.errors)
                + repr([(name, formset.errors) for (name, formset) in edit_handler.form.formsets.iteritems() if formset.errors])
            )
    else:
        form = form_class(instance=page)
        edit_handler = edit_handler_class(instance=page, form=form)


    # Check for revisions still undergoing moderation and warn
    if latest_revision and latest_revision.submitted_for_moderation:
        messages.warning(request, "This page is currently awaiting moderation")

    return render(request, 'verdantadmin/pages/edit.html', {
        'page': page,
        'edit_handler': edit_handler,
        'errors_debug': errors_debug,
    })

@login_required
def reorder(request, parent_page_id=None):
    if parent_page_id:
        parent_page = get_object_or_404(Page, id=parent_page_id)
    else:
        parent_page = Page.get_first_root_node()

    pages = parent_page.get_children()

    if request.POST:
        try:
            pages_ordered = [Page.objects.get(id=int(page[5:])) for page in request.POST['order'].split(',')]
        except:
            # Invalid
            messages.error(request, "Could not reorder (invalid request)")
            return redirect('verdantadmin_pages_reorder', parent_page_id)

        # Reorder
        for page in pages_ordered:
            page.move(parent_page, pos='last-child')

        # Success message
        messages.success(request, "Pages reordered successfully")

        return redirect('verdantadmin_explore', parent_page_id)
    else:
        return render(request, 'verdantadmin/pages/reorder.html', {
            'parent_page': parent_page,
            'pages': pages,
        })

@login_required
def delete(request, page_id):
    page = get_object_or_404(Page, id=page_id)

    if not request.user.has_perm('core.can_unpublish_page'):
        # they should only be able to delete this page if this page is unpublished, AND it has no
        # published children
        if page.live:
            parent_id = page.get_parent().id
            messages.error(request, "You do not have permission to delete this page, because it is live on the site.")
            return redirect('verdantadmin_explore', parent_id)
        elif page.get_descendants().filter(live=True).exists():
            parent_id = page.get_parent().id
            messages.error(request, "You do not have permission to delete this page, because it has subpages that are live on the site.")
            return redirect('verdantadmin_explore', parent_id)

    if request.POST:
        parent_id = page.get_parent().id
        page.delete()
        messages.success(request, "Page '%s' deleted." % page.title)
        return redirect('verdantadmin_explore', parent_id)

    return render(request, 'verdantadmin/pages/confirm_delete.html', {
        'page': page,
        'descendant_count': page.get_descendant_count()
    })

@login_required
def view_draft(request, page_id):
    page = get_object_or_404(Page, id=page_id).get_latest_revision_as_page()
    return page.serve(request)

@login_required
def preview_on_edit(request, page_id):
    # Receive the form submission that would typically be posted to the 'edit' view. If submission is valid,
    # return the rendered page; if not, re-render the edit form
    page = get_object_or_404(Page, id=page_id).get_latest_revision_as_page()
    edit_handler_class = get_page_edit_handler(page.__class__)
    form_class = edit_handler_class.get_form_class(page.__class__)

    form = form_class(request.POST, request.FILES, instance=page)

    if form.is_valid():
        form.save(commit=False)

        # FIXME: passing the original request to page.serve is dodgy (particularly if page.serve has
        # special treatment of POSTs). Ought to construct one that more or less matches what would be sent
        # as a front-end GET request
        response = page.serve(request)

        response['X-Verdant-Preview'] = 'ok'
        return response

    else:
        edit_handler = edit_handler_class(instance=page, form=form)

        response = render(request, 'verdantadmin/pages/edit.html', {
            'page': page,
            'edit_handler': edit_handler,
        })
        response['X-Verdant-Preview'] = 'error'
        return response

@login_required
def preview_on_create(request, content_type_app_name, content_type_model_name, parent_page_id):
    # Receive the form submission that would typically be posted to the 'create' view. If submission is valid,
    # return the rendered page; if not, re-render the edit form
    try:
        content_type = ContentType.objects.get_by_natural_key(content_type_app_name, content_type_model_name)
    except ContentType.DoesNotExist:
        raise Http404

    page_class = content_type.model_class()
    page = page_class()
    edit_handler_class = get_page_edit_handler(page_class)
    form_class = edit_handler_class.get_form_class(page_class)

    form = form_class(request.POST, request.FILES, instance=page)

    if form.is_valid():
        form.save(commit=False)

        # FIXME: passing the original request to page.serve is dodgy (particularly if page.serve has
        # special treatment of POSTs). Ought to construct one that more or less matches what would be sent
        # as a front-end GET request
        response = page.serve(request)

        response['X-Verdant-Preview'] = 'ok'
        return response

    else:
        edit_handler = edit_handler_class(instance=page, form=form)
        parent_page = get_object_or_404(Page, id=parent_page_id).specific

        response = render(request, 'verdantadmin/pages/create.html', {
            'content_type': content_type,
            'page_class': page_class,
            'parent_page': parent_page,
            'edit_handler': edit_handler,
        })
        response['X-Verdant-Preview'] = 'error'
        return response

@permission_required('core.can_unpublish_page')
def unpublish(request, page_id):
    page = get_object_or_404(Page, id=page_id)

    if request.POST:
        parent_id = page.get_parent().id
        page.live = False
        page.save()
        messages.success(request, "Page '%s' unpublished." % page.title)
        return redirect('verdantadmin_explore', parent_id)

    return render(request, 'verdantadmin/pages/confirm_unpublish.html', {
        'page': page,
    })

@login_required
def move_choose_destination(request, page_to_move_id, viewed_page_id=None):
    page_to_move = get_object_or_404(Page, id=page_to_move_id)

    if viewed_page_id:
        viewed_page = get_object_or_404(Page, id=viewed_page_id)
    else:
        viewed_page = Page.get_first_root_node()

    child_pages = []
    for page in viewed_page.get_children():
        # can't move the page into itself or its descendants
        can_choose = not(page == page_to_move or page.is_child_of(page_to_move))

        can_descend = can_choose and page.get_children_count()

        child_pages.append({
            'page': page, 'can_choose': can_choose, 'can_descend': can_descend,
        })

    return render(request, 'verdantadmin/pages/move_choose_destination.html', {
        'page_to_move': page_to_move,
        'viewed_page': viewed_page,
        'child_pages': child_pages,
    })

@login_required
def move_confirm(request, page_to_move_id, destination_id):
    page_to_move = get_object_or_404(Page, id=page_to_move_id)
    destination = get_object_or_404(Page, id=destination_id)

    if request.POST:
        try:
            page_to_move.move(destination, pos='last-child')

            messages.success(request, "Page '%s' moved." % page_to_move.title)
            return redirect('verdantadmin_explore', destination.id)
        except InvalidMoveToDescendant:
            messages.error(request, "You cannot move this page into itself.")
            return redirect('verdantadmin_pages_move', page_to_move.id)

    else:
        if page_to_move == destination or destination.is_descendant_of(page_to_move):
            messages.error(request, "You cannot move this page into itself.")
            return redirect('verdantadmin_pages_move', page_to_move.id)

    return render(request, 'verdantadmin/pages/confirm_move.html', {
        'page_to_move': page_to_move,
        'destination': destination,
    })


PAGE_EDIT_HANDLERS = {}
def get_page_edit_handler(page_class):
    if page_class not in PAGE_EDIT_HANDLERS:
        PAGE_EDIT_HANDLERS[page_class] = TabbedInterface([
            ObjectList(page_class.content_panels, heading='Content'),
            ObjectList(page_class.promote_panels, heading='Promote')
        ])

    return PAGE_EDIT_HANDLERS[page_class]


@login_required
def search(request):
    pages = []
    q = None
    is_searching = False
    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            # page number
            p = request.GET.get("p", 1)
            is_searching = True
            pages = Page.title_search_backend(q, prefetch_related=['content_type'])

            # Pagination
            paginator = Paginator(pages, 20)
            try:
                pages =  paginator.page(p)
            except PageNotAnInteger:
                pages =  paginator.page(1)
            except EmptyPage:
                pages =  paginator.page(paginator.num_pages)
    else:
        form = SearchForm()

    if request.is_ajax():
        return render(request, "verdantadmin/pages/search_results.html", {
            'pages': pages,
            'is_searching': is_searching,
            'search_query': q,
        })
    else:
        return render(request, "verdantadmin/pages/search.html", {
            'form': form,
            'pages': pages,
            'is_searching': is_searching,
            'search_query': q,
        })


@permission_required('core.can_publish_page')
def approve_moderation(request, revision_id):
    revision = get_object_or_404(PageRevision, id=revision_id)
    if not revision.submitted_for_moderation:
        messages.error(request, "The page '%s' is not currently awaiting moderation." % revision.page.title)
        return redirect('verdantadmin_home')

    if request.POST:
        revision.publish()
        messages.success(request, "Page '%s' published." % revision.page.title)

    return redirect('verdantadmin_home')

@permission_required('core.can_publish_page')
def reject_moderation(request, revision_id):
    revision = get_object_or_404(PageRevision, id=revision_id)
    if not revision.submitted_for_moderation:
        messages.error(request, "The page '%s' is not currently awaiting moderation." % revision.page.title)
        return redirect('verdantadmin_home')

    if request.POST:
        revision.submitted_for_moderation = False
        revision.save(update_fields=['submitted_for_moderation'])
        messages.success(request, "Page '%s' rejected for publication." % revision.page.title)

    return redirect('verdantadmin_home')

@permission_required('core.can_publish_page')
def preview_for_moderation(request, revision_id):
    revision = get_object_or_404(PageRevision, id=revision_id)
    if not revision.submitted_for_moderation:
        messages.error(request, "The page '%s' is not currently awaiting moderation." % revision.page.title)
        return redirect('verdantadmin_home')

    page = revision.as_page_object()
    if not hasattr(request, 'userbar'):
        request.userbar = []
    request.userbar.append(
        render_to_string('verdantadmin/pages/_moderator_userbar.html', {
            'revision': revision,
        }, context_instance=RequestContext(request))
    )

    return page.serve(request)