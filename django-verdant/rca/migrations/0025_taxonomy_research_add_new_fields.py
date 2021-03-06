# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0017_auto_20160630_1103'),
        ('rca', '0024_pagealias'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchitem',
            name='programme_new',
            field=models.ForeignKey(related_name='research_items', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='taxonomy.Programme', help_text=b'', null=True),
        ),
        migrations.AddField(
            model_name='researchitem',
            name='school_new',
            field=models.ForeignKey(related_name='research_items', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='taxonomy.School', help_text=b'', null=True),
        ),
    ]
