# Generated by Django 4.1.2 on 2022-12-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_coursemodel_location_coursemodel_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
