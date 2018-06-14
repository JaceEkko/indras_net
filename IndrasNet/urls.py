from django.conf.urls import url

from . import views

app_name = 'IndrasNet'


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^parameters/*$', views.parameters, name='parameters'),
    url(r'^help/*$', views.help, name='help'),
    url(r'^feedback/*$', views.feedback, name='feedback'),
]
