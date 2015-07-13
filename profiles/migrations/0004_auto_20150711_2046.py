# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150711_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employerprofile',
            options={'verbose_name': 'test'},
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='business_address_region',
            field=models.CharField(max_length=50, choices=[(b'1', b'Auckland'), (b'2', b'Wellington'), (b'3', b'Christchurch')]),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='business_address_suburb',
            field=models.CharField(max_length=50, choices=[(b'1', b'Glendowie'), (b'2', b'Kohimarama'), (b'3', b'Mission Bay')]),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='business_industry',
            field=models.CharField(max_length=50, choices=[(b'1', b'Restaurant'), (b'2', b'IT'), (b'3', b'Construction')]),
        ),
    ]
