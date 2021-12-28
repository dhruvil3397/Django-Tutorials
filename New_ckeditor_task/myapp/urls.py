from django.urls import path,include
from . import views

urlpatterns = [
    path('showform/', views.showform, name = "showform"),
    path('showback/', views.showback, name = "showback"),
    path('editdata/' ,views.editdata,name ='edit_data'),
    path('updatedata/' ,views.updatedata,name ='update_data'),
    path('deletedata/',views.deletedata, name='delete_data'),
    path('viewdata/',views.viewdata, name='view_data'),
    path('signup/', views.signup, name = "signup"),
    path('loginhandle/', views.loginhandle, name = "loginhandle"),
    path('logouthandle/', views.logouthandle, name = "logouthandle"),
    
]
