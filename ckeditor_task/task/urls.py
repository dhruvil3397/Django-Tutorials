from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('show/',views.show),
    path('showdetails/<int:id>',views.showdetails),
    path('updatedetails/<int:id>',views.updatedetails),
    path('deletedata/',views.deletedata, name='delete_data'),
]