# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table('threads_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group_owner', to=orm['auth.User'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group_location', null=True, to=orm['common.Location'])),
        ))
        db.send_create_signal('threads', ['Group'])

        # Adding M2M table for field moderators on 'Group'
        db.create_table('threads_group_moderators', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['threads.group'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('threads_group_moderators', ['group_id', 'user_id'])

        # Adding M2M table for field members on 'Group'
        db.create_table('threads_group_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['threads.group'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('threads_group_members', ['group_id', 'user_id'])

        # Adding M2M table for field banned_users on 'Group'
        db.create_table('threads_group_banned_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['threads.group'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('threads_group_banned_users', ['group_id', 'user_id'])

        # Adding model 'Thread'
        db.create_table('threads_thread', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')(max_length=4096)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='thread_author', to=orm['auth.User'])),
        ))
        db.send_create_signal('threads', ['Thread'])

        # Adding M2M table for field participants on 'Thread'
        db.create_table('threads_thread_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('thread', models.ForeignKey(orm['threads.thread'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('threads_thread_participants', ['thread_id', 'user_id'])

        # Adding model 'Message'
        db.create_table('threads_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_thread', to=orm['threads.Thread'])),
            ('body', self.gf('django.db.models.fields.TextField')(max_length=4096)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_author', to=orm['auth.User'])),
        ))
        db.send_create_signal('threads', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table('threads_group')

        # Removing M2M table for field moderators on 'Group'
        db.delete_table('threads_group_moderators')

        # Removing M2M table for field members on 'Group'
        db.delete_table('threads_group_members')

        # Removing M2M table for field banned_users on 'Group'
        db.delete_table('threads_group_banned_users')

        # Deleting model 'Thread'
        db.delete_table('threads_thread')

        # Removing M2M table for field participants on 'Thread'
        db.delete_table('threads_thread_participants')

        # Deleting model 'Message'
        db.delete_table('threads_message')


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
        'common.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_parent'", 'null': 'True', 'to': "orm['common.Location']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'threads.group': {
            'Meta': {'object_name': 'Group'},
            'banned_users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'group_banned_members'", 'null': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_location'", 'null': 'True', 'to': "orm['common.Location']"}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'group_members'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'moderators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'group_moderators'", 'null': 'True', 'to': "orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_owner'", 'to': "orm['auth.User']"})
        },
        'threads.message': {
            'Meta': {'object_name': 'Message'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_author'", 'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'max_length': '4096'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_thread'", 'to': "orm['threads.Thread']"})
        },
        'threads.thread': {
            'Meta': {'object_name': 'Thread'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thread_author'", 'to': "orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'max_length': '4096'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'thread_participants'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['threads']