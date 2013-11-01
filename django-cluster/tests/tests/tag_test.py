from django.test import TestCase
from taggit.models import Tag
from django.forms.models import ModelForm

from tests.models import Place, TaggedPlace

class TagTest(TestCase):
    def test_can_access_tags_on_unsaved_instance(self):
        mission_burrito = Place(name='Mission Burrito')
        self.assertEqual(0, mission_burrito.tags.count())

        mission_burrito.tags.add('mexican', 'burrito')
        self.assertEqual(2, mission_burrito.tags.count())
        self.assertEqual(Tag, mission_burrito.tags.all()[0].__class__)
        self.assertTrue([tag for tag in mission_burrito.tags.all() if tag.name == 'mexican'])

        mission_burrito.save()
        self.assertEqual(2, TaggedPlace.objects.filter(content_object_id=mission_burrito.id).count())

        mission_burrito.tags.remove('burrito')
        self.assertEqual(1, mission_burrito.tags.count())
        # should not affect database until we save
        self.assertEqual(2, TaggedPlace.objects.filter(content_object_id=mission_burrito.id).count())
        mission_burrito.save()
        self.assertEqual(1, TaggedPlace.objects.filter(content_object_id=mission_burrito.id).count())

        mission_burrito.tags.clear()
        self.assertEqual(0, mission_burrito.tags.count())
        # should not affect database until we save
        self.assertEqual(1, TaggedPlace.objects.filter(content_object_id=mission_burrito.id).count())
        mission_burrito.save()
        self.assertEqual(0, TaggedPlace.objects.filter(content_object_id=mission_burrito.id).count())

    def test_tag_form_field(self):
        class PlaceForm(ModelForm):
            class Meta:
                model = Place

        mission_burrito = Place(name='Mission Burrito')
        mission_burrito.tags.add('mexican', 'burrito')

        form = PlaceForm(instance=mission_burrito)
        self.assertEqual(2, len(form['tags'].value()))
        self.assertEqual(TaggedPlace, form['tags'].value()[0].__class__)
