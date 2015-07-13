# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150711_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerprofile',
            name='business_address_region',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='business_address_suburb',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='business_industry',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
