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

class JobListing(models.Model):

    region_choice = (
        ('1', 'Auckland'),
        ('2', 'Wellington'),
        ('3', 'Christchurch')
    )
    industry_choice = (
        ('1', 'Accounting'),
        ('2', 'Agriculture, fishing & forestry'),
        ('3', 'Automotive'),
        ('4', 'Banking, finance & insurance'),
        ('5', 'Construction & Architecture'),
        ('6', 'Customer service'),
    )
    employment_type_choice = (
        ('1', 'Full Time'),
        ('2', 'Part Time'),
        ('3', 'One-off'),
        ('4', 'Other')
    )
    contact_method_choice = (
        ('1', 'Phone'),
        ('2', 'Email'),
    )

    user = models.OneToOneField(User, unique=False)
    business_name = models.CharField(max_length=50)
    pay_rate = models.FloatField()
    employment_type = models.CharField(max_length=10, choices=employment_type_choice)
    job_description = models.CharField(max_length=2000)
    business_address_region = models.CharField(max_length=50, choices=region_choice)
    business_address_suburb = models.CharField(max_length=50)
    business_industry = models.CharField(max_length=50, choices=industry_choice)
    contact_method = models.CharField(max_length=50, choices=contact_method_choice)
    active_listing = models.BooleanField(default=True)
    job_id = models.AutoField("ID", primary_key=True, editable=False, unique=True)

    class Meta:
        verbose_name = 'Job Listing'

    def __unicode__(self):
        return "%s" % self.business_name




