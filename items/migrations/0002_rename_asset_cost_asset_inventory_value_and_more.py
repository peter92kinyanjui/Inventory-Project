# Generated by Django 5.1.3 on 2024-11-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='asset_cost',
            new_name='Inventory_value',
        ),
        migrations.AddField(
            model_name='asset',
            name='unit_cost',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]