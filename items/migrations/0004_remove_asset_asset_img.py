# Generated by Django 5.1.3 on 2024-12-04 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_rename_inventory_value_asset_inv_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='asset_img',
        ),
    ]