from django.contrib import admin
from profiles.models import SignUpProfile, JobListing

class SignUpProfileAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "account_type"]

    class Meta:
        model = SignUpProfile

class JobListingAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "job_title", "user"]

    class Meta:
        model = JobListing

admin.site.register(SignUpProfile, SignUpProfileAdmin)
admin.site.register(JobListing, JobListingAdmin)
