# Generated by Django 5.1.3 on 2024-12-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='staff_email',
            field=models.EmailField(max_length=100),
        ),
    ]