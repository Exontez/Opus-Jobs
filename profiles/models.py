from django.db import models
from django.contrib.auth.models import User

class SignUpProfile(models.Model):
    account_type_choice = (
        ('1', 'Student'),
        ('2', 'Employer')
    )

    user = models.OneToOneField(User, unique=True)
    account_type = models.CharField(max_length=10, choices=account_type_choice)
    contact_number = models.IntegerField(max_length=12)

    class Meta:
        verbose_name = 'SignUp Profile'

    def __unicode__(self):
        return "%s" % self.user

class JobProfile(models.Model):

    region_choice = (
        ('1', 'Auckland'),
        ('2', 'Wellington'),
        ('3', 'Christchurch')
    )
    industry_choice = (
        ('1', 'Restaurant'),
        ('2', 'IT'),
        ('3', 'Construction')
    )

    business_name = models.CharField(max_length=50)
    business_address_number = models.IntegerField()
    business_address_street = models.CharField(max_length=50)
    business_address_region = models.CharField(max_length=50, choices=region_choice)
    business_address_suburb = models.CharField(max_length=50)
    business_address_postcode = models.IntegerField(max_length=4)
    business_industry = models.CharField(max_length=50, choices=industry_choice)

    class Meta:
        verbose_name = 'Job Profile'

    def __unicode__(self):
        return "%s" % self.user




