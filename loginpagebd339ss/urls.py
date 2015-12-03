from django.conf.urls import patterns, url

from loginpagebd339ss import views

urlpatterns = patterns('',
    url(r'^$', views.login_url, name='login_url'),
)
