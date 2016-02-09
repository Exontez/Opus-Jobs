from django.conf.urls import patterns, url
from profiles import views

# These are the URL's for my create job listing, edit profile and edit listing page
urlpatterns = [
    url(r'^createjoblisting/', views.createjoblisting, name='createjoblisting'),
    url(r'^(?P<pk>[0-9]+)/editprofile/', views.editprofile, name='editprofile'),
    url(r'^(?P<pk>[0-9]+)/editlisting/', views.editlisting, name='editlisting'),
    url(r'^editlistingportal/', views.editlistingportal, name='editlistingportal'),
    url(r'^(?P<pk>[0-9]+)/deletelistingconfirm/', views.deletelistingconfirm, name='deletelistingconfirm'),
    url(r'^(?P<pk>[0-9]+)/deletefunction/', views.deletefunction, name='deletefunction'),
]
