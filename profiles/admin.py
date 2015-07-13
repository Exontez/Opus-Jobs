from django.contrib import admin

from profiles.models import EmployerProfile

class EmployerProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(EmployerProfile, EmployerProfileAdmin)
