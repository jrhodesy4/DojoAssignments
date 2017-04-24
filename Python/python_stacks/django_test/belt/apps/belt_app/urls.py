from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),
    url(r'^main$', views.main),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^message$', views.message),
    url(r'^books/(?P<id>\d+)$', views.books, name= 'my_book'),
    url(r'^user/(?P<id>\d+)$', views.user_page),
    url(r'^message/(?P<id>\d+)$', views.message, name= 'my_message'),
    url(r'^delete/(?P<id>\d+)/(?P<page>\w+)$', views.delete)
]
