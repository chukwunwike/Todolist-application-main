from . import views
from django.urls import path

app_name = 'mytodo'


urlpatterns=[
    path('login/',views.loginpage, name ='login'),
    path('index/',views.index, name = 'index'),
    path('logout/',views.logoutpage, name = 'logout'),
    path('delete/<int:id>',views.delete_view,name = 'delete'),
    path('register/',views.registerpage,name = 'register'),
  
    
    ]