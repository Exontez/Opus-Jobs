from django.db import models
from django.contrib.auth.models import User

class EmployerProfile(models.Model):

    account_type_choice = (
        ('1', 'Male'),
        ('2', 'Female')
    )
    region_choice = (
        ('1', 'Auckland'),
        ('2', 'Wellington'),
        ('3', 'Christchurch')
    )
    suburb_choice = (
        ('1', 'Glendowie'),
        ('2', 'Kohimarama'),
        ('3', 'Mission Bay')
    )
    industry_choice = (
        ('1', 'Restaurant'),
        ('2', 'IT'),
        ('3', 'Construction')
    )

    account_type = models.CharField(max_length=50, choices=account_type_choice)
    user = models.OneToOneField(User, unique=True)
    home_number = models.IntegerField(max_length=12)
    mobile_number = models.IntegerField(max_length=12)
    business_name = models.CharField(max_length=50)
    business_address_number = models.IntegerField()
    business_address_street = models.CharField(max_length=50)
    business_address_region = models.CharField(max_length=50, choices=region_choice)
    business_address_suburb = models.CharField(max_length=50, choices=suburb_choice)
    business_address_postcode = models.IntegerField(max_length=4)
    business_industry = models.CharField(max_length=50, choices=industry_choice)

    class Meta:
        verbose_name = 'Employer Profile'

    def __unicode__(self):
        return "%s" % self.user



