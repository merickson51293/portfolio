# Generated by Django 2.2 on 2020-12-16 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_petite_app', '0008_auto_20201216_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(upload_to='sweet_petite_app/static/uploads/'),
        ),
    ]