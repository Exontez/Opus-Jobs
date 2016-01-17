from django.conf.urls import patterns, include, url
from django.contrib import admin
import django.contrib.auth.views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^', include('main.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^listings/', include('listings.urls')),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

]