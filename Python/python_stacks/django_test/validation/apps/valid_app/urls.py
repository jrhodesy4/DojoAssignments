from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),
    url(r'^valid$', views.valid),
    url(r'^results$', views.results),
    url(r'^regress$', views.regress)

]
