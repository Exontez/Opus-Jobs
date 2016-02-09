from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

referral_choices = (
    ('1', 'Friends & Family'),
    ('2', 'Other Websites'),
    ('3', 'Advertisements'),
    ('4', 'High School or University'),
    ('5', 'Other'),
)

class StudentForm(models.Model):
    user = models.OneToOneField(User, unique=True)
    birth_date = models.DateField()
    contact_number = models.IntegerField()
    referral = models.CharField(max_length=100, choices=referral_choices)


class EmployerForm(models.Model):
    user = models.OneToOneField(User, unique=True)
    contact_number = models.IntegerField()
    referral = models.CharField(max_length=100, choices=referral_choices)