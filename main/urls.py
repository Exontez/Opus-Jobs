from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='index'),
    url(r'^about/$', 'main.views.about', name="about"),

)
