# Generated by Django 3.1.3 on 2020-11-28 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orderupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
