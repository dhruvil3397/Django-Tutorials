from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/',views.home),
    path('result/',views.Resultlistview.as_view()),
    path('result/<int:pk>', views.Resultdetailview.as_view()),
    path('', RedirectView.as_view(url = "home/")),
]
