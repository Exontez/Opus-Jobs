from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

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
        ('1', 'Auckland'),
        ('2', 'Wellington'),
        ('3', 'Christchurch')
    )
    suburb_choice = (
        ('1', 'Glendowie'),
        ('2', 'Kohimarama'),
        ('3', 'Herne Bay')
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
    area_code_choice = (
        ('1', '021'),
        ('2', '027'),
        ('3', '022'),
        ('4', 'Other')
    )

    user = models.CharField(max_length=50)
    job_title = models.CharField(max_length=30)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    employment_type = models.CharField(max_length=10, choices=employment_type_choice)
    job_description = models.CharField(max_length=2000)
    business_address_region = models.CharField(max_length=50, choices=region_choice)
    business_address_suburb = models.CharField(max_length=50, choices=suburb_choice)
    business_industry = models.CharField(max_length=50, choices=industry_choice)
    email = models.EmailField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    area_code = models.CharField(max_length=5, choices=area_code_choice, blank=True)
    listing_view_counter = models.IntegerField(default=0)
    active_listing = models.BooleanField(default=True)
    listing_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Job Listing'

    def clean(self):
        if not (self.email or self.telephone):
            raise ValidationError("You must specify either email or telephone")
        if not self.email:
            self.email = "Not Provided"
        if not self.telephone:
            self.telephone = "Not Provided"

    def __unicode__(self):
        return "%s" % self.job_title




