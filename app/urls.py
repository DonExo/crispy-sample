from django.conf.urls import url
from django.contrib.auth import views as djangoviews
from app import views

urlpatterns = [
    url(r'', views.index, name='index'),
]