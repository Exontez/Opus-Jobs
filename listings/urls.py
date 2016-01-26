from django.conf.urls import patterns, url
from listings import views

# This is declaring the URL for my browse view
urlpatterns = [
    url(r'^browse', views.browse, name='browse'),
    url(r'^(?P<pk>[0-9]+)/listing/', views.listing, name='listing'),

]
