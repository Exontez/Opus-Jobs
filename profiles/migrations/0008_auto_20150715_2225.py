# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0007_employerprofile_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.CharField(max_length=10, choices=[(b'1', b'Student'), (b'2', b'Employer')])),
                ('contact_number', models.IntegerField(max_length=12)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SignUp Profile',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='EmployerProfile',
        ),
    ]
