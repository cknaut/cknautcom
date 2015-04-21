from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from temp_hum import views
from landingpage import views as landingpageviews

urlpatterns = [
    url(r'^add_data/temp=(?P<temp>[0-9^&]+)&hum=(?P<hum>[0-9^&]+)/$', views.add_data, name="adder"),
    url(r'^$', views.temp_index, name='temp_index'),
    url(r'^temp_ajax/$', views.ajax_temp_index, name="ajax_request"),
]
