from django.contrib import admin

from profiles.models import SignUpProfile

class SignUpProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(SignUpProfile, SignUpProfileAdmin)
