# Generated by Django 2.2 on 2021-01-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_petite_app', '0029_goods_best_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='best_seller',
            field=models.BooleanField(default=False),
        ),
    ]