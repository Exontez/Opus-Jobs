# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_number', models.IntegerField(max_length=12)),
                ('mobile_number', models.IntegerField(max_length=12)),
                ('business_name', models.CharField(max_length=50)),
                ('business_address_number', models.IntegerField()),
                ('business_address_street', models.CharField(max_length=50)),
                ('business_address_region', models.CharField(max_length=50)),
                ('business_address_suburb', models.CharField(max_length=50)),
                ('business_address_postcode', models.IntegerField()),
                ('business_industry', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
