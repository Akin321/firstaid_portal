from django.urls import path
from. import views
app_name='edit'
urlpatterns=[
    path('add/',views.add,name='add'),
    path('update/<int:med_id>/',views.update,name='update'),
    path('delete/<int:med_id>/',views.delete,name='delete'),
    path('add_cat/',views.add_cat,name='category'),
    path('update_cat/<int:cat_id>/', views.update_cat, name='update_cat'),
    path('delete_cat/<int:cat_id>/', views.delete_cat, name='delete_cat'),
]