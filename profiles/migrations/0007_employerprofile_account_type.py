# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20150714_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerprofile',
            name='account_type',
            field=models.CharField(default=1, max_length=10, choices=[(b'1', b'Student'), (b'2', b'Employer')]),
            preserve_default=False,
        ),
    ]
