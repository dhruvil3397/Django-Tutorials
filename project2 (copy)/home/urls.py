from django.urls import path,include
from .import views

urlpatterns = [     
    path('', views.home , name = "Home"),
    path('contact/', views.contact , name = "Contact"),
    path('about/', views.about , name = "about"),
    path('search/', views.search, name = "Search"),
    path('signup/', views.signup, name = "signup"),
    path('loginhandle/', views.loginhandle, name = "loginhandle"),
    path('logouthandle/', views.logouthandle, name = "logouthandle"),


]
