from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit),
    url(r'^results$', views.results),
    url(r'^regress$', views.regress)
]

# url(r'^submit$', views.index')
