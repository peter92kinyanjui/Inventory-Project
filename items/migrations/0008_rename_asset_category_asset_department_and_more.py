# Generated by Django 5.1.3 on 2024-12-05 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_rename_status_request_allocation_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='asset_category',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='asset_category',
            new_name='department',
        ),
    ]
