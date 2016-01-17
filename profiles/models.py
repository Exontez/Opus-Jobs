from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

#This is the model for my extended signup profile
class SignUpProfile(models.Model):
    account_type_choice = (
        ('1', 'Student'),
        ('2', 'Employer')
    )

    user = models.OneToOneField(User, unique=True)
    account_type = models.CharField(max_length=10, choices=account_type_choice)
    contact_number = models.IntegerField()

    class Meta:
        verbose_name = 'SignUp Profile'

    def __unicode__(self):
        return "%s" % self.user

# This is the model for my edit and add job listing page
class JobListing(models.Model):

    region_choice = (
        ('Auckland', 'Auckland'),
        ('Wellington', 'Wellington'),
        ('Christchurch', 'Christchurch')
    )
    industry_choice = (
        ('Accounting', 'Accounting'),
        ('Agriculture, fishing & forestry', 'Agriculture, fishing & forestry'),
        ('Automotive', 'Automotive'),
        ('Banking, finance & insurance', 'Banking, finance & insurance'),
        ('Construction & Architecture', 'Construction & Architecture'),
        ('Customer service', 'Customer service'),
    )
    employment_type_choice = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('One-off', 'One-off'),
        ('Other', 'Other')
    )

    user = models.CharField(max_length=50)
    job_title = models.CharField(max_length=30)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    employment_type = models.CharField(max_length=10, choices=employment_type_choice)
    job_description = models.CharField(max_length=2000)
    business_address_region = models.CharField(max_length=50, choices=region_choice)
    business_address_suburb = models.CharField(max_length=50)
    business_industry = models.CharField(max_length=50, choices=industry_choice)
    email = models.EmailField(max_length=50, blank=True)
    telephone = models.IntegerField(blank=True)
    active_listing = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Job Listing'

    def clean(self):
        if not (self.email or self.telephone):
            raise ValidationError("You must specify either email or telephone")

    def __unicode__(self):
        return "%s" % self.business_name




