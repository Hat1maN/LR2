from django.urls import path
from .views import password_view

urlpatterns = [
    path('password/', password_view, name='password_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.encyclopedia_view, name='encyclopedia'),
]
