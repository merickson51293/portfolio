# Generated by Django 2.2 on 2021-01-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_auto_20210106_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='/sweet_petite/index', max_length=255),
            preserve_default=False,
        ),
    ]
