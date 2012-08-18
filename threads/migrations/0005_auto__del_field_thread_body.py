# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Thread.body'
        db.delete_column('threads_thread', 'body')


    def backwards(self, orm):
        # Adding field 'Thread.body'
        db.add_column('threads_thread', 'body',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=4096),
                      keep_default=False)


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
        'threads.entity': {
            'Meta': {'object_name': 'Entity'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_group'", 'to': "orm['threads.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_user'", 'to': "orm['auth.User']"})
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
        'threads.inbox': {
            'Meta': {'object_name': 'Inbox'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'threads': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'inbox_threads'", 'symmetrical': 'False', 'to': "orm['threads.Thread']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inbox_user'", 'to': "orm['auth.User']"})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'thread_participants'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['threads']