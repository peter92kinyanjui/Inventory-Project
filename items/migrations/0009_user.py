# Generated by Django 5.1.3 on 2024-12-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_rename_asset_category_asset_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_no', models.CharField(max_length=50)),
                ('staff_fname', models.CharField(max_length=100)),
                ('staff_sname', models.CharField(max_length=100)),
                ('staff_email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
