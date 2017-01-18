# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'postman_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'sent_messages', null=True, to=orm['users.User'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'received_messages', null=True, to=orm['users.User'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'next_messages', null=True, to=orm['postman.Message'])),
            ('thread', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'child_messages', null=True, to=orm['postman.Message'])),
            ('sent_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('read_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('replied_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sender_archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('recipient_archived', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sender_deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('recipient_deleted_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('moderation_status', self.gf('django.db.models.fields.CharField')(default=u'p', max_length=1)),
            ('moderation_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'moderated_messages', null=True, to=orm['users.User'])),
            ('moderation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('moderation_reason', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
        ))
        db.send_create_signal(u'postman', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'postman_message')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dacl.commodity': {
            'Meta': {'ordering': "['name']", 'object_name': 'Commodity'},
            'code': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'unique_with': '()', 'max_length': '255', 'populate_from': "'name'", 'blank': 'True'}),
            'slug_en': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_ru': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_uk': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usex_code': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'dacl.country': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['code', 'region'],)", 'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_3166': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '2', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'region_countries'", 'to': "orm['dacl.Region']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'unique_with': '()', 'max_length': '255', 'populate_from': "'name'", 'blank': 'True'}),
            'slug_en': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_ru': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_uk': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'usex_code': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'dacl.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "u''", 'max_length': '255', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "u''", 'max_length': '255', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "u''", 'max_length': '255', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'unique_with': '()', 'max_length': '255', 'populate_from': "'name'", 'blank': 'True'}),
            'slug_en': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_ru': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_uk': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'postman.message': {
            'Meta': {'ordering': "[u'-sent_at', u'-id']", 'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderation_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'moderated_messages'", 'null': 'True', 'to': u"orm['users.User']"}),
            'moderation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'moderation_reason': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'moderation_status': ('django.db.models.fields.CharField', [], {'default': "u'p'", 'max_length': '1'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'next_messages'", 'null': 'True', 'to': u"orm['postman.Message']"}),
            'read_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'received_messages'", 'null': 'True', 'to': u"orm['users.User']"}),
            'recipient_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recipient_deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'replied_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'sent_messages'", 'null': 'True', 'to': u"orm['users.User']"}),
            'sender_archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sender_deleted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'child_messages'", 'null': 'True', 'to': u"orm['postman.Message']"})
        },
        u'snapshot.marketsnapshotsection': {
            'Meta': {'ordering': "[u'order']", 'object_name': 'MarketSnapshotSection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'unique_with': '()', 'max_length': '255', 'populate_from': "'name'", 'blank': 'True'}),
            'slug_en': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_ru': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug_uk': ('autoslug.fields.AutoSlugField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'about': ('redactor.fields.RedactorField', [], {'null': 'True', 'db_index': 'True'}),
            'activity': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'broker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commodities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'user_commodities'", 'to': "orm['dacl.Commodity']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True', 'db_index': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'company_address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'confirmation_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dacl.Country']", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'home_page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['snapshot.MarketSnapshotSection']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "u'en'", 'max_length': '5'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_login_ip': ('django.db.models.fields.IPAddressField', [], {'default': "u'127.0.0.1'", 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'logo': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'password_reset_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'promo_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'remarks': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'subscribe': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'trial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unsubscribe_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'max_length': '32', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['postman']
