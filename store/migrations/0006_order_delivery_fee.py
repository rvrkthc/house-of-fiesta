# Generated by Django 4.0.5 on 2022-06-19 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_inventory_is_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_fee',
            field=models.DecimalField(decimal_places=2, default=49.99, max_digits=7),
            preserve_default=False,
        ),
    ]
