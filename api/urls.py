from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^featured/$', views.get_featured),
]
