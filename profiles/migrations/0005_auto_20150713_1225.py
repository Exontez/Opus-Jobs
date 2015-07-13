# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150711_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employerprofile',
            options={'verbose_name': 'Employer Profile'},
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='account_type',
            field=models.CharField(default=1, max_length=50, choices=[(b'1', b'Male'), (b'2', b'Female')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='business_address_postcode',
            field=models.IntegerField(max_length=4),
        ),
    ]
