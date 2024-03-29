# encoding: utf-8
# Copyright 2013 maker
# License

import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Notification'
        db.delete_table('core_notification')

        # Adding model 'Comment'
        db.create_table('core_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('core', ['Comment'])

        # Adding M2M table for field likes on 'Comment'
        db.create_table('core_comment_likes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comment', models.ForeignKey(orm['core.comment'], null=False)),
            ('user', models.ForeignKey(orm['core.user'], null=False))
        ))
        db.create_unique('core_comment_likes', ['comment_id', 'user_id'])

        # Adding M2M table for field dislikes on 'Comment'
        db.create_table('core_comment_dislikes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comment', models.ForeignKey(orm['core.comment'], null=False)),
            ('user', models.ForeignKey(orm['core.user'], null=False))
        ))
        db.create_unique('core_comment_dislikes', ['comment_id', 'user_id'])

        # Adding model 'Tag'
        db.create_table('core_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('core', ['Tag'])

        # Adding model 'RevisionField'
        db.create_table('core_revisionfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('revision', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Revision'])),
            ('field_type', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('value_key', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='revisionfield_key', null=True, to=orm['core.Object'])),
            ('value_key_acc', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='revisionfield_key_acc', null=True, to=orm['core.AccessEntity'])),
        ))
        db.send_create_signal('core', ['RevisionField'])

        # Adding M2M table for field value_m2m on 'RevisionField'
        db.create_table('core_revisionfield_value_m2m', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('revisionfield', models.ForeignKey(orm['core.revisionfield'], null=False)),
            ('object', models.ForeignKey(orm['core.object'], null=False))
        ))
        db.create_unique('core_revisionfield_value_m2m', ['revisionfield_id', 'object_id'])

        # Adding M2M table for field value_m2m_acc on 'RevisionField'
        db.create_table('core_revisionfield_value_m2m_acc', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('revisionfield', models.ForeignKey(orm['core.revisionfield'], null=False)),
            ('accessentity', models.ForeignKey(orm['core.accessentity'], null=False))
        ))
        db.create_unique('core_revisionfield_value_m2m_acc', ['revisionfield_id', 'accessentity_id'])

        # Adding model 'Revision'
        db.create_table('core_revision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('previous', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='next_set', unique=True, null=True, to=orm['core.Revision'])),
            ('object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Object'])),
            ('change_type', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('core', ['Revision'])

        # Adding model 'Invitation'
        db.create_table('core_invitation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True, blank=True)),
            ('default_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Group'], null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('core', ['Invitation'])

        # Adding model 'AccessEntity'
        db.create_table('core_accessentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['AccessEntity'])

        # Adding model 'UpdateRecord'
        db.create_table('core_updaterecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sent_updates', null=True, to=orm['core.User'])),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sent_updates', null=True, to=orm['core.Object'])),
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('format_message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('format_strings', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('core', ['UpdateRecord'])

        # Adding M2M table for field about on 'UpdateRecord'
        db.create_table('core_updaterecord_about', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('updaterecord', models.ForeignKey(orm['core.updaterecord'], null=False)),
            ('object', models.ForeignKey(orm['core.object'], null=False))
        ))
        db.create_unique('core_updaterecord_about', ['updaterecord_id', 'object_id'])

        # Adding M2M table for field recipients on 'UpdateRecord'
        db.create_table('core_updaterecord_recipients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('updaterecord', models.ForeignKey(orm['core.updaterecord'], null=False)),
            ('accessentity', models.ForeignKey(orm['core.accessentity'], null=False))
        ))
        db.create_unique('core_updaterecord_recipients', ['updaterecord_id', 'accessentity_id'])

        # Adding M2M table for field comments on 'UpdateRecord'
        db.create_table('core_updaterecord_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('updaterecord', models.ForeignKey(orm['core.updaterecord'], null=False)),
            ('comment', models.ForeignKey(orm['core.comment'], null=False))
        ))
        db.create_unique('core_updaterecord_comments', ['updaterecord_id', 'comment_id'])

        # Adding M2M table for field likes on 'UpdateRecord'
        db.create_table('core_updaterecord_likes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('updaterecord', models.ForeignKey(orm['core.updaterecord'], null=False)),
            ('user', models.ForeignKey(orm['core.user'], null=False))
        ))
        db.create_unique('core_updaterecord_likes', ['updaterecord_id', 'user_id'])

        # Adding M2M table for field dislikes on 'UpdateRecord'
        db.create_table('core_updaterecord_dislikes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('updaterecord', models.ForeignKey(orm['core.updaterecord'], null=False)),
            ('user', models.ForeignKey(orm['core.user'], null=False))
        ))
        db.create_unique('core_updaterecord_dislikes', ['updaterecord_id', 'user_id'])

        # Deleting field 'Group.last_updated'
        db.delete_column('core_group', 'last_updated')

        # Adding field 'Group.accessentity_ptr'
        db.add_column('core_group', 'accessentity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.AccessEntity'], unique=True, null=True, blank=True), keep_default=False)

        # Deleting field 'Object.group_read'
        db.delete_column('core_object', 'group_read')

        # Deleting field 'Object.user_write'
        db.delete_column('core_object', 'user_write')

        # Deleting field 'Object.group'
        db.delete_column('core_object', 'group_id')

        # Deleting field 'Object.everybody_execute'
        db.delete_column('core_object', 'everybody_execute')

        # Deleting field 'Object.user_execute'
        db.delete_column('core_object', 'user_execute')

        # Deleting field 'Object.user_read'
        db.delete_column('core_object', 'user_read')

        # Deleting field 'Object.everybody_write'
        db.delete_column('core_object', 'everybody_write')

        # Deleting field 'Object.group_write'
        db.delete_column('core_object', 'group_write')

        # Deleting field 'Object.group_execute'
        db.delete_column('core_object', 'group_execute')

        # Deleting field 'Object.everybody_read'
        db.delete_column('core_object', 'everybody_read')

        # Adding field 'Object.creator'
        db.add_column('core_object', 'creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='objects_created', null=True, to=orm['core.User']), keep_default=False)

        # Adding M2M table for field read_access on 'Object'
        db.create_table('core_object_read_access', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('object', models.ForeignKey(orm['core.object'], null=False)),
            ('accessentity', models.ForeignKey(orm['core.accessentity'], null=False))
        ))
        db.create_unique('core_object_read_access', ['object_id', 'accessentity_id'])

        # Adding M2M table for field full_access on 'Object'
        db.create_table('core_object_full_access', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('object', models.ForeignKey(orm['core.object'], null=False)),
            ('accessentity', models.ForeignKey(orm['core.accessentity'], null=False))
        ))
        db.create_unique('core_object_full_access', ['object_id', 'accessentity_id'])

        # Adding M2M table for field tags on 'Object'
        db.create_table('core_object_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('object', models.ForeignKey(orm['core.object'], null=False)),
            ('tag', models.ForeignKey(orm['core.tag'], null=False))
        ))
        db.create_unique('core_object_tags', ['object_id', 'tag_id'])

        # Adding M2M table for field comments on 'Object'
        db.create_table('core_object_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('object', models.ForeignKey(orm['core.object'], null=False)),
            ('comment', models.ForeignKey(orm['core.comment'], null=False))
        ))
        db.create_unique('core_object_comments', ['object_id', 'comment_id'])

        # Adding M2M table for field likes on 'Object'
        db.create_table('core_object_likes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('object', models.ForeignKey(orm['core.object'], null=False)),
            ('user', models.ForeignKey(orm['core.user'], null=False))
        ))
        db.create_unique('core_object_likes', ['object_id', 'user_id'])

        # Adding M2M table for field dislikes on 'Object'
        db.create_table('core_object_dislikes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('object', models.ForeignKey(orm['core.object'], null=False)),
            ('user', models.ForeignKey(orm['core.user'], null=False))
        ))
        db.create_unique('core_object_dislikes', ['object_id', 'user_id'])

        # Changing field 'Object.user'
        db.alter_column('core_object', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'], null=True))

        # Deleting field 'User.last_updated'
        db.delete_column('core_user', 'last_updated')

        # Adding field 'User.accessentity_ptr'
        db.add_column('core_user', 'accessentity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.AccessEntity'], unique=True, null=True, blank=True), keep_default=False)

        # Adding field 'User.disabled'
        db.add_column('core_user', 'disabled', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'User.last_access'
        db.add_column('core_user', 'last_access', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now), keep_default=False)

        # Changing field 'User.default_group'
        db.alter_column('core_user', 'default_group_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.AccessEntity']))


    def backwards(self, orm):
        
        # Adding model 'Notification'
        db.create_table('core_notification', (
            ('object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Object'], null=True, blank=True)),
            ('format_strings', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('object_type', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('format_message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notification_sent_set', null=True, to=orm['core.User'], blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('core', ['Notification'])

        # Deleting model 'Comment'
        db.delete_table('core_comment')

        # Removing M2M table for field likes on 'Comment'
        db.delete_table('core_comment_likes')

        # Removing M2M table for field dislikes on 'Comment'
        db.delete_table('core_comment_dislikes')

        # Deleting model 'Tag'
        db.delete_table('core_tag')

        # Deleting model 'RevisionField'
        db.delete_table('core_revisionfield')

        # Removing M2M table for field value_m2m on 'RevisionField'
        db.delete_table('core_revisionfield_value_m2m')

        # Removing M2M table for field value_m2m_acc on 'RevisionField'
        db.delete_table('core_revisionfield_value_m2m_acc')

        # Deleting model 'Revision'
        db.delete_table('core_revision')

        # Deleting model 'Invitation'
        db.delete_table('core_invitation')

        # Deleting model 'AccessEntity'
        db.delete_table('core_accessentity')

        # Deleting model 'UpdateRecord'
        db.delete_table('core_updaterecord')

        # Removing M2M table for field about on 'UpdateRecord'
        db.delete_table('core_updaterecord_about')

        # Removing M2M table for field recipients on 'UpdateRecord'
        db.delete_table('core_updaterecord_recipients')

        # Removing M2M table for field comments on 'UpdateRecord'
        db.delete_table('core_updaterecord_comments')

        # Removing M2M table for field likes on 'UpdateRecord'
        db.delete_table('core_updaterecord_likes')

        # Removing M2M table for field dislikes on 'UpdateRecord'
        db.delete_table('core_updaterecord_dislikes')

        # User chose to not deal with backwards NULL issues for 'Group.last_updated'
        raise RuntimeError("Cannot reverse this migration. 'Group.last_updated' and its values cannot be restored.")

        # Deleting field 'Group.accessentity_ptr'
        db.delete_column('core_group', 'accessentity_ptr_id')

        # Adding field 'Object.group_read'
        db.add_column('core_object', 'group_read', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Object.user_write'
        db.add_column('core_object', 'user_write', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Object.group'
        raise RuntimeError("Cannot reverse this migration. 'Object.group' and its values cannot be restored.")

        # Adding field 'Object.everybody_execute'
        db.add_column('core_object', 'everybody_execute', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Object.user_execute'
        db.add_column('core_object', 'user_execute', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Object.user_read'
        db.add_column('core_object', 'user_read', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Object.everybody_write'
        db.add_column('core_object', 'everybody_write', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Object.group_write'
        db.add_column('core_object', 'group_write', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Object.group_execute'
        db.add_column('core_object', 'group_execute', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Object.everybody_read'
        db.add_column('core_object', 'everybody_read', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Object.creator'
        db.delete_column('core_object', 'creator_id')

        # Removing M2M table for field read_access on 'Object'
        db.delete_table('core_object_read_access')

        # Removing M2M table for field full_access on 'Object'
        db.delete_table('core_object_full_access')

        # Removing M2M table for field tags on 'Object'
        db.delete_table('core_object_tags')

        # Removing M2M table for field comments on 'Object'
        db.delete_table('core_object_comments')

        # Removing M2M table for field likes on 'Object'
        db.delete_table('core_object_likes')

        # Removing M2M table for field dislikes on 'Object'
        db.delete_table('core_object_dislikes')

        # User chose to not deal with backwards NULL issues for 'Object.user'
        raise RuntimeError("Cannot reverse this migration. 'Object.user' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'User.last_updated'
        raise RuntimeError("Cannot reverse this migration. 'User.last_updated' and its values cannot be restored.")

        # Deleting field 'User.accessentity_ptr'
        db.delete_column('core_user', 'accessentity_ptr_id')

        # Deleting field 'User.disabled'
        db.delete_column('core_user', 'disabled')

        # Deleting field 'User.last_access'
        db.delete_column('core_user', 'last_access')

        # Changing field 'User.default_group'
        db.alter_column('core_user', 'default_group_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['core.Group']))


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
        'core.accessentity': {
            'Meta': {'object_name': 'AccessEntity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
        'core.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group'},
            'accessentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.AccessEntity']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['core.Group']"})
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
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'objects_created'", 'null': 'True', 'to': "orm['core.User']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dislikes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_disliked'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'full_access': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_full_access'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.AccessEntity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_liked'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'links_rel_+'", 'null': 'True', 'to': "orm['core.Object']"}),
            'nuvius_resource': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'object_type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'read_access': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'objects_read_access'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.AccessEntity']"}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'subscriptions'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Tag']", 'null': 'True', 'blank': 'True'}),
            'trash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']", 'null': 'True', 'blank': 'True'})
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
            'previous': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'next_set'", 'unique': 'True', 'null': 'True', 'to': "orm['core.Revision']"})
        },
        'core.revisionfield': {
            'Meta': {'object_name': 'RevisionField'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Revision']"}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'value_key': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'revisionfield_key'", 'null': 'True', 'to': "orm['core.Object']"}),
            'value_key_acc': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'revisionfield_key_acc'", 'null': 'True', 'to': "orm['core.AccessEntity']"}),
            'value_m2m': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'revisionfield_m2m'", 'symmetrical': 'False', 'to': "orm['core.Object']"}),
            'value_m2m_acc': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'revisionfield_m2m_acc'", 'symmetrical': 'False', 'to': "orm['core.AccessEntity']"})
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
            'recipients': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'received_updates'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.AccessEntity']"}),
            'record_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sent_updates'", 'null': 'True', 'to': "orm['core.Object']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        'core.user': {
            'Meta': {'ordering': "['name']", 'object_name': 'User'},
            'accessentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.AccessEntity']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'default_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_user_set'", 'null': 'True', 'to': "orm['core.AccessEntity']"}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
