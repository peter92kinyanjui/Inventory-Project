# Generated by Django 5.1.3 on 2024-12-05 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_alter_user_staff_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
