from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('group_detail', views.group_detail, name="group_detail"),
]
