from django.urls import path, include
from . import views
app_name='firstaid_app'
urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='view_by_cat'),
    path('<slug:c_slug>/<slug:m_slug>/',views.meddetial,name='view_med'),

]