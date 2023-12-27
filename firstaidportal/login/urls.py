from django.urls import path

from . import views
app_name='login'
urlpatterns=[
    path('',views.login,name='login'),
    path('registration/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('admin_page/',views.admin,name='admin_page')
]
