# Generated by Django 2.2 on 2021-01-06 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proj_blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_blog', to='portfolio_app.Blog'),
            preserve_default=False,
        ),
    ]
