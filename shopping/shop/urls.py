from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url = 'home/'),name="Shophome"),
    path('home/', views.index,name="Shophome"),
    path('about/', views.about,name="Aboutus"),
    path('contact/', views.contact,name="Contactus"),
    path('tracker/', views.tracker,name="Tracking status"),
    path('search/', views.search,name="Search"),
    path('products/<int:myid>', views.productview,name="Productview"),
    #path('checkout/', views.checkout,name="Checkout"),
]
