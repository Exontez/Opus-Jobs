from django.conf.urls import patterns, url
import main.views

# These are my URL's for the index, about and 404 page
urlpatterns = [
    url(r'^$', main.views.index, name='index'),
    url(r'^about/$', main.views.about, name="about"),
    url(r'^credits/$', main.views.credits, name="credits"),
    url(r'^sorry/$', main.views.featurenotimplemented, name="featurenotimplemented"),
    url(r'^permission_denied/$', main.views.permissiondenied, name="permissiondenied"),

]
