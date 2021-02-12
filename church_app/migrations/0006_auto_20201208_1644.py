# Generated by Django 2.2 on 2020-12-08 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0005_directmessages_dm'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('im', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_message', to='church_app.User')),
            ],
        ),
        migrations.DeleteModel(
            name='DirectMessages',
        ),
    ]