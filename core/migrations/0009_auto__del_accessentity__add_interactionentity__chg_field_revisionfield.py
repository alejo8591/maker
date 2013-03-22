# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AccessEntity'
        db.delete_table('core_accessentity')

        # Adding model 'InteractionEntity'
        db.create_table('core_interactionentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['InteractionEntity'])


        # Changing field 'RevisionField.value_key_acc'
        db.alter_column('core_revisionfield', 'value_key_acc_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['core.InteractionEntity']))

        # Changing field 'RevisionField.value_key'
        db.alter_column('core_revisionfield', 'value_key_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['core.Object']))
        # Deleting field 'Group.accessentity_ptr'
        db.delete_column('core_group', 'accessentity_ptr_id')

        # Adding field 'Group.interactionentity_ptr'
        db.add_column('core_group', 'interactionentity_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 3, 21, 0, 0), to=orm['core.InteractionEntity'], unique=True, primary_key=True),
                      keep_default=False)


        # Changing field 'Object.creator'
        db.alter_column('core_object', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['core.User']))
        # Deleting field 'User.accessentity_ptr'
        db.delete_column('core_user', 'accessentity_ptr_id')

        # Adding field 'User.interactionentity_ptr'
        db.add_column('core_user', 'interactionentity_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 3, 21, 0, 0), to=orm['core.InteractionEntity'], unique=True, primary_key=True),
                      keep_default=False)


        # Changing field 'UpdateRecord.sender'
        db.alter_column('core_updaterecord', 'sender_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['core.Object']))

    def backwards(self, orm):
        # Adding model 'AccessEntity'
        db.create_table('core_accessentity', (
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['AccessEntity'])

        # Deleting model 'InteractionEntity'
        db.delete_table('core_interactionentity')


        # Changing field 'RevisionField.value_key_acc'
        db.alter_column('core_revisionfield', 'value_key_acc_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.AccessEntity']))

        # Changing field 'RevisionField.value_key'
        db.alter_column('core_revisionfield', 'value_key_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Object']))
        # Adding field 'Group.accessentity_ptr'
        db.add_column('core_group', 'accessentity_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 3, 21, 0, 0), to=orm['core.AccessEntity'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Group.interactionentity_ptr'
        db.delete_column('core_group', 'interactionentity_ptr_id')


        # Changing field 'Object.creator'
        db.alter_column('core_object', 'creator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.User']))
        # Adding field 'User.accessentity_ptr'
        db.add_column('core_user', 'accessentity_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2013, 3, 21, 0, 0), to=orm['core.AccessEntity'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'User.interactionentity_ptr'
        db.delete_column('core_user', 'interactionentity_ptr_id')


        # Changing field 'UpdateRecord.sender'
        db.alter_column('core_updaterecord', 'sender_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Object']))

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
        'core.attachment': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Attachment'},
            'attached_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'attached_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Object']", 'null': 'True', 'blank': 'True'}),
            'attached_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.UpdateRecord']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'uploaded_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"})
        },
        'core.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']", 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dislikes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'comments_disliked'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'comments_liked'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"})
        },
        'core.configsetting': {
            'Meta': {'object_name': 'ConfigSetting'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group', '_ormbases': ['core.InteractionEntity']},
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'interactionentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.InteractionEntity']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['core.Group']"})
        },
        'core.interactionentity': {
            'Meta': {'object_name': 'InteractionEntity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'core.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'default_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Group']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']", 'null': 'True', 'blank': 'True'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location', '_ormbases': ['core.Object']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['core.Location']"})
        },
        'core.module': {
            'Meta': {'ordering': "['name']", 'object_name': 'Module', '_ormbases': ['core.Object']},
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'system': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'core.modulesetting': {
            'Meta': {'object_name': 'ModuleSetting'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Module']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'perspective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Perspective']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']", 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'core.object': {
            'Meta': {'object_name': 'Object'},
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.Comment']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'objects_created'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['core.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dislikes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_disliked'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'full_access': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_full_access'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.InteractionEntity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_liked'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'links_rel_+'", 'null': 'True', 'to': "orm['core.Object']"}),
            'nuvius_resource': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'read_access': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_read_access'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.InteractionEntity']"}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'subscriptions'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Tag']", 'null': 'True', 'blank': 'True'}),
            'trash': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.page': {
            'Meta': {'ordering': "['name']", 'object_name': 'Page', '_ormbases': ['core.Object']},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.PageFolder']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'core.pagefolder': {
            'Meta': {'object_name': 'PageFolder', '_ormbases': ['core.Object']},
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.perspective': {
            'Meta': {'object_name': 'Perspective', '_ormbases': ['core.Object']},
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modules': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Module']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.revision': {
            'Meta': {'object_name': 'Revision'},
            'change_type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Object']"}),
            'previous': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'next'", 'unique': 'True', 'null': 'True', 'to': "orm['core.Revision']"})
        },
        'core.revisionfield': {
            'Meta': {'object_name': 'RevisionField'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Revision']"}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'value_key': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'revisionfield_key'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['core.Object']"}),
            'value_key_acc': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'revisionfield_key_acc'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['core.InteractionEntity']"}),
            'value_m2m': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'revisionfield_m2m'", 'symmetrical': 'False', 'to': "orm['core.Object']"}),
            'value_m2m_acc': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'revisionfield_m2m_acc'", 'symmetrical': 'False', 'to': "orm['core.InteractionEntity']"})
        },
        'core.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'core.updaterecord': {
            'Meta': {'ordering': "['-date_created']", 'object_name': 'UpdateRecord'},
            'about': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'updates'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.Object']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sent_updates'", 'null': 'True', 'to': "orm['core.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'comments_on_updates'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.Comment']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dislikes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'updates_disliked'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'format_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'format_strings': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'updates_liked'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'recipients': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'received_updates'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.InteractionEntity']"}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sent_updates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['core.Object']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        'core.user': {
            'Meta': {'ordering': "['name']", 'object_name': 'User', '_ormbases': ['core.InteractionEntity']},
            'default_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_user_set'", 'null': 'True', 'to': "orm['core.Group']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interactionentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.InteractionEntity']", 'unique': 'True', 'primary_key': 'True'}),
            'last_access': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Group']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.widget': {
            'Meta': {'ordering': "['weight']", 'object_name': 'Widget'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'perspective': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Perspective']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'widget_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['core']