# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0005_auto_20150713_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Employee Profile',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_name', models.CharField(max_length=50)),
                ('business_address_number', models.IntegerField()),
                ('business_address_street', models.CharField(max_length=50)),
                ('business_address_region', models.CharField(max_length=50, choices=[(b'1', b'Auckland'), (b'2', b'Wellington'), (b'3', b'Christchurch')])),
                ('business_address_suburb', models.CharField(max_length=50)),
                ('business_address_postcode', models.IntegerField(max_length=4)),
                ('business_industry', models.CharField(max_length=50, choices=[(b'1', b'Restaurant'), (b'2', b'IT'), (b'3', b'Construction')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Job Profile',
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='employerprofile',
            old_name='home_number',
            new_name='contact_number',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_address_number',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_address_postcode',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_address_region',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_address_street',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_address_suburb',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_industry',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='business_name',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='mobile_number',
        ),
    ]
