# Generated by Django 2.2 on 2020-12-21 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_petite_app', '0021_order_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='goods',
        ),
    ]