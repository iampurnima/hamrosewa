# Generated by Django 5.1.3 on 2024-11-22 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_servicecategory_icon_serviceprovider_profile_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecategory',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='services',
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.servicecategory'),
        ),
    ]
