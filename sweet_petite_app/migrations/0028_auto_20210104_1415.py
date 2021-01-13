# Generated by Django 2.2 on 2021-01-04 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_petite_app', '0027_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default='Delicious Cookies'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='goods',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_goods', to='sweet_petite_app.Goods'),
            preserve_default=False,
        ),
    ]
