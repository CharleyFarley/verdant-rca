# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SavedEmbed', fields ['url', 'maxwidth']
        db.delete_unique(u'verdantembeds_savedembed', ['url', 'maxwidth'])

        # Deleting model 'SavedEmbed'
        db.delete_table(u'verdantembeds_savedembed')

        # Adding model 'Embed'
        db.create_table(u'verdantembeds_embed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'verdantembeds', ['Embed'])


    def backwards(self, orm):
        # Adding model 'SavedEmbed'
        db.create_table(u'verdantembeds_savedembed', (
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('maxwidth', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'verdantembeds', ['SavedEmbed'])

        # Adding unique constraint on 'SavedEmbed', fields ['url', 'maxwidth']
        db.create_unique(u'verdantembeds_savedembed', ['url', 'maxwidth'])

        # Deleting model 'Embed'
        db.delete_table(u'verdantembeds_embed')


    models = {
        u'verdantembeds.embed': {
            'Meta': {'object_name': 'Embed'},
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['verdantembeds']