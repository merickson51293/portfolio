# Generated by Django 2.2 on 2020-12-21 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_petite_app', '0017_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]