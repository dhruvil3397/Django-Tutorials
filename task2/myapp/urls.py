from django.contrib import admin
from django.urls.conf import include
from django.urls import path
from .import views


urlpatterns = [
    path('',views.home),
    path('export/', views.export_xls, name="export"),

]

