from django.conf.urls import patterns, include, url
from django.contrib import admin
#from profiles.forms import EmployerForm
#from registration.views import RegistrationView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^', include('main.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

)
