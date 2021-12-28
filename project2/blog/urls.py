from django.urls import path,include
from .import views

urlpatterns = [     
        path('', views.bloghome , name = "BlogHome"),
        path('<str:slug>', views.blogpost, name = "BlogPost"),

        # API to post a comment
        path('postcomment/', views.postcomment , name = "postcomment"),
]
