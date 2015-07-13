# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_address_region',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_address_suburb',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_industry',
        ),
    ]
