# Generated by Django 4.0.5 on 2022-06-19 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='is_enabled',
        ),
    ]
