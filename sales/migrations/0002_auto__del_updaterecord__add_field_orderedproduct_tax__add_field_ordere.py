# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from decimal import Decimal
from maker.sales.models import OrderedProduct, Product

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        if not db.dry_run:
            ops = OrderedProduct.objects.all()
            ps = Product.objects.all()
        
        # Deleting model 'UpdateRecord'
        db.delete_table('sales_updaterecord')

        # Adding field 'OrderedProduct.tax'
        db.add_column('sales_orderedproduct', 'tax', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Tax'], null=True, blank=True), keep_default=False)

        # Adding field 'OrderedProduct.rate'
        db.add_column('sales_orderedproduct', 'rate', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=20, decimal_places=2), keep_default=False)

        # Adding field 'OrderedProduct.rate_display'
        db.add_column('sales_orderedproduct', 'rate_display', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=2), keep_default=False)

        # Adding field 'OrderedProduct.description'
        db.add_column('sales_orderedproduct', 'description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        if not db.dry_run:
            # convert old Float fields to temporary fields
            for op in ops:
                op.discount_f = op.discount
                op.discount = 0
                op.quantity_f = op.quantity
                op.quantity = 0
                op.save()
        
        # Changing field 'OrderedProduct.discount'
        db.alter_column('sales_orderedproduct', 'discount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2))

        # Changing field 'OrderedProduct.quantity'
        db.alter_column('sales_orderedproduct', 'quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2))

        if not db.dry_run:
            for p in ps:
                p.buy_price_f = p.buy_price
                p.buy_price = 0
                p.sell_price_f = p.sell_price
                p.sell_price = 0
                p.save()

        # Changing field 'Product.buy_price'
        db.alter_column('sales_product', 'buy_price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2))

        # Changing field 'Product.sell_price'
        db.alter_column('sales_product', 'sell_price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2))

        # Adding field 'Opportunity.amount_currency'
        db.add_column('sales_opportunity', 'amount_currency', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['finance.Currency']), keep_default=False)

        # Adding field 'Opportunity.amount_display'
        db.add_column('sales_opportunity', 'amount_display', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=20, decimal_places=2), keep_default=False)

        # Changing field 'Opportunity.probability'
        db.alter_column('sales_opportunity', 'probability', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=0))

        # Changing field 'Opportunity.amount'
        db.alter_column('sales_opportunity', 'amount', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2))

        # Deleting field 'SaleOrder.payment'
        db.delete_column('sales_saleorder', 'payment_id')

        # Adding field 'SaleOrder.currency'
        db.add_column('sales_saleorder', 'currency', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['finance.Currency']), keep_default=False)

        # Adding field 'SaleOrder.total'
        db.add_column('sales_saleorder', 'total', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=2), keep_default=False)

        # Adding field 'SaleOrder.total_display'
        db.add_column('sales_saleorder', 'total_display', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=2), keep_default=False)

        # Adding M2M table for field payment on 'SaleOrder'
        db.create_table('sales_saleorder_payment', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('saleorder', models.ForeignKey(orm['sales.saleorder'], null=False)),
            ('transaction', models.ForeignKey(orm['finance.transaction'], null=False))
        ))
        db.create_unique('sales_saleorder_payment', ['saleorder_id', 'transaction_id'])

        if not db.dry_run:
            # convert temporary fields back into decimal
            for op in ops:
                if op.discount_f:
                    op.discount = Decimal(unicode(op.discount_f)).quantize(Decimal('.01'), 'ROUND_DOWN')
                if op.quantity_f:
                    op.quantity = int(op.quantity_f)
                op.save()
            
            for p in ps:
                if p.buy_price_f:
                    p.buy_price = Decimal(unicode(p.buy_price_f))
                if p.sell_price_f:
                    p.sell_price = Decimal(unicode(p.sell_price_f))
                p.save()


    def backwards(self, orm):
        
        # Adding model 'UpdateRecord'
        db.create_table('sales_updaterecord', (
            ('lead', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.Lead'], null=True, blank=True)),
            ('object_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Object'], unique=True, primary_key=True)),
            ('record_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('details', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('opportunity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.Opportunity'], null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.SaleOrder'], null=True, blank=True)),
        ))
        db.send_create_signal('sales', ['UpdateRecord'])

        # Deleting field 'OrderedProduct.tax'
        db.delete_column('sales_orderedproduct', 'tax_id')

        # Deleting field 'OrderedProduct.rate'
        db.delete_column('sales_orderedproduct', 'rate')

        # Deleting field 'OrderedProduct.rate_display'
        db.delete_column('sales_orderedproduct', 'rate_display')

        # Deleting field 'OrderedProduct.description'
        db.delete_column('sales_orderedproduct', 'description')

        # Changing field 'OrderedProduct.discount'
        db.alter_column('sales_orderedproduct', 'discount', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'OrderedProduct.quantity'
        db.alter_column('sales_orderedproduct', 'quantity', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Product.buy_price'
        db.alter_column('sales_product', 'buy_price', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Product.sell_price'
        db.alter_column('sales_product', 'sell_price', self.gf('django.db.models.fields.FloatField')(null=True))

        # Deleting field 'Opportunity.amount_currency'
        db.delete_column('sales_opportunity', 'amount_currency_id')

        # Deleting field 'Opportunity.amount_display'
        db.delete_column('sales_opportunity', 'amount_display')

        # Changing field 'Opportunity.probability'
        db.alter_column('sales_opportunity', 'probability', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Opportunity.amount'
        db.alter_column('sales_opportunity', 'amount', self.gf('django.db.models.fields.FloatField')())

        # Adding field 'SaleOrder.payment'
        db.add_column('sales_saleorder', 'payment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Transaction'], null=True, blank=True), keep_default=False)

        # Deleting field 'SaleOrder.currency'
        db.delete_column('sales_saleorder', 'currency_id')

        # Deleting field 'SaleOrder.total'
        db.delete_column('sales_saleorder', 'total')

        # Deleting field 'SaleOrder.total_display'
        db.delete_column('sales_saleorder', 'total_display')

        # Removing M2M table for field payment on 'SaleOrder'
        db.delete_table('sales_saleorder_payment')


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
        },
        'core.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
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
        'finance.account': {
            'Meta': {'ordering': "['name']", 'object_name': 'Account', '_ormbases': ['core.Object']},
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'balance_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Currency']"}),
            'balance_display': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['identities.Contact']"})
        },
        'finance.category': {
            'Meta': {'object_name': 'Category', '_ormbases': ['core.Object']},
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'})
        },
        'finance.currency': {
            'Meta': {'object_name': 'Currency', '_ormbases': ['core.Object']},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'factor': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '10', 'decimal_places': '4'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'finance.liability': {
            'Meta': {'ordering': "['-due_date']", 'object_name': 'Liability', '_ormbases': ['core.Object']},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Account']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Category']", 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_liability_source'", 'to': "orm['identities.Contact']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_liability_target'", 'to': "orm['identities.Contact']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'value_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Currency']"}),
            'value_display': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'})
        },
        'finance.tax': {
            'Meta': {'object_name': 'Tax', '_ormbases': ['core.Object']},
            'compound': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        'finance.transaction': {
            'Meta': {'ordering': "['-datetime']", 'object_name': 'Transaction', '_ormbases': ['core.Object']},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Account']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Category']", 'null': 'True', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'liability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Liability']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_transaction_source'", 'to': "orm['identities.Contact']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'finance_transaction_target'", 'to': "orm['identities.Contact']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'value_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Currency']"}),
            'value_display': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'})
        },
        'identities.contact': {
            'Meta': {'ordering': "['name']", 'object_name': 'Contact', '_ormbases': ['core.Object']},
            'contact_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['identities.ContactType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['identities.Contact']"}),
            'related_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Group']", 'null': 'True', 'blank': 'True'}),
            'related_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.AccessEntity']", 'null': 'True', 'blank': 'True'})
        },
        'identities.contactfield': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactField', '_ormbases': ['core.Object']},
            'allowed_values': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'identities.contacttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ContactType', '_ormbases': ['core.Object']},
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['identities.ContactField']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'sales.lead': {
            'Meta': {'ordering': "['contact']", 'object_name': 'Lead', '_ormbases': ['core.Object']},
            'assigned': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sales_lead_assigned'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['identities.Contact']"}),
            'contact_method': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'products_interested': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sales.Product']", 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.SaleSource']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.SaleStatus']"})
        },
        'sales.opportunity': {
            'Meta': {'ordering': "['-expected_date']", 'object_name': 'Opportunity', '_ormbases': ['core.Object']},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'amount_currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Currency']"}),
            'amount_display': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'assigned': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sales_opportunity_assigned'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'closed_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['identities.Contact']"}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expected_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.Lead']", 'null': 'True', 'blank': 'True'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'probability': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '0', 'blank': 'True'}),
            'products_interested': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sales.Product']", 'symmetrical': 'False'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.SaleSource']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.SaleStatus']"})
        },
        'sales.orderedproduct': {
            'Meta': {'ordering': "['product']", 'object_name': 'OrderedProduct', '_ormbases': ['core.Object']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.SaleOrder']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.Product']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '4', 'decimal_places': '2'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'rate_display': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.Subscription']", 'null': 'True', 'blank': 'True'}),
            'tax': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Tax']", 'null': 'True', 'blank': 'True'})
        },
        'sales.product': {
            'Meta': {'ordering': "['code']", 'object_name': 'Product', '_ormbases': ['core.Object']},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'buy_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child_set'", 'null': 'True', 'to': "orm['sales.Product']"}),
            'product_type': ('django.db.models.fields.CharField', [], {'default': "'good'", 'max_length': '32'}),
            'runout_action': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'sell_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'stock_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['identities.Contact']", 'null': 'True', 'blank': 'True'}),
            'supplier_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'sales.saleorder': {
            'Meta': {'ordering': "['-datetime']", 'object_name': 'SaleOrder', '_ormbases': ['core.Object']},
            'assigned': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'sales_saleorder_assigned'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['core.User']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['identities.Contact']", 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['finance.Currency']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'opportunity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.Opportunity']", 'null': 'True', 'blank': 'True'}),
            'payment': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['finance.Transaction']", 'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.SaleSource']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.SaleStatus']"}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'total_display': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'})
        },
        'sales.salesource': {
            'Meta': {'ordering': "('-active', 'name')", 'object_name': 'SaleSource', '_ormbases': ['core.Object']},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'})
        },
        'sales.salestatus': {
            'Meta': {'ordering': "('hidden', '-active', 'name')", 'object_name': 'SaleStatus', '_ormbases': ['core.Object']},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'use_leads': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_opportunities': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_sales': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'sales.subscription': {
            'Meta': {'ordering': "['expiry']", 'object_name': 'Subscription', '_ormbases': ['core.Object']},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['identities.Contact']", 'null': 'True', 'blank': 'True'}),
            'cycle_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cycle_period': ('django.db.models.fields.CharField', [], {'default': "'month'", 'max_length': '32'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'expiry': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sales.Product']", 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['sales']
