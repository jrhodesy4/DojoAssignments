from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout)     # 'home' route.
]
