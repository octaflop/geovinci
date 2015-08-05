# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampusLocation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('street_address', models.CharField(max_length=240)),
                ('additional_address', models.CharField(max_length=240, blank=True, help_text='Apartment or Suite Number')),
                ('locality', models.CharField(max_length=240, help_text='The city or municipality of the campus')),
                ('region', models.CharField(max_length=100, help_text='State or Province of the campus (Abbreviation preffered)')),
                ('telephone', models.CharField(max_length=50, blank=True, help_text='Phone number of the campus')),
                ('zip_code', models.CharField(max_length=10, blank=True, help_text='Zip or Postal Code of the campus')),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326, blank=True, null=True)),
            ],
        ),
    ]
