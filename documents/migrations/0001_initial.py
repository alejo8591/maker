# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Folder'
        db.create_table('documents_folder', (
            ('object_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Object'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child_set', null=True, to=orm['documents.Folder'])),
        ))
        db.send_create_signal('documents', ['Folder'])

        # Adding model 'File'
        db.create_table('documents_file', (
            ('object_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Object'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Folder'])),
            ('content', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('documents', ['File'])

        # Adding model 'Document'
        db.create_table('documents_document', (
            ('object_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Object'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Folder'])),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('documents', ['Document'])

        # Adding model 'WebLink'
        db.create_table('documents_weblink', (
            ('object_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Object'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Folder'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('documents', ['WebLink'])


    def backwards(self, orm):
        
        # Deleting model 'Folder'
        db.delete_table('documents_folder')

        # Deleting model 'File'
        db.delete_table('documents_file')

        # Deleting model 'Document'
        db.delete_table('documents_document')

        # Deleting model 'WebLink'
        db.delete_table('documents_weblink')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group'},
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['core.Group']"})
        },
        'core.object': {
            'Meta': {'object_name': 'Object'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'everybody_execute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'everybody_read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'everybody_write': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Group']"}),
            'group_execute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group_read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group_write': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'links_rel_+'", 'null': 'True', 'to': "orm['core.Object']"}),
            'nuvius_resource': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'subscriptions'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'trash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"}),
            'user_execute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_write': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.user': {
            'Meta': {'ordering': "['name']", 'object_name': 'User'},
            'default_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_user_set'", 'null': 'True', 'to': "orm['core.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Group']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'documents.document': {
            'Meta': {'ordering': "['-last_updated']", 'object_name': 'Document', '_ormbases': ['core.Object']},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.Folder']"}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'documents.file': {
            'Meta': {'ordering': "['-last_updated']", 'object_name': 'File', '_ormbases': ['core.Object']},
            'content': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.Folder']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'})
        },
        'documents.folder': {
            'Meta': {'object_name': 'Folder', '_ormbases': ['core.Object']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['documents.Folder']"})
        },
        'documents.weblink': {
            'Meta': {'ordering': "['-last_updated']", 'object_name': 'WebLink', '_ormbases': ['core.Object']},
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.Folder']"}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['documents']
