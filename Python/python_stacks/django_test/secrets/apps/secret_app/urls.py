from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
	url(r'^message$', views.message),
    url(r'^secrets$', views.secrets),
    url(r'^like/(?P<id>\d+)/(?P<page>\w+)$', views.like),
    url(r'^popular$', views.popular),
    url(r'^delete/(?P<id>\d+)/(?P<page>\w+)$', views.delete),
    url(r'^back$', views.back),
    url(r'^logout$', views.logout)

    # url(r'^logout$', views.logout)       # 'home' route.
]
