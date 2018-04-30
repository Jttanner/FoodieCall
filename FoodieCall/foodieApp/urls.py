# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='login'),
    url(r'^chat/$', views.index, name='index'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]