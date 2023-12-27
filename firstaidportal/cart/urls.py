from django.urls import path
from . import views
app_name='cart'
urlpatterns=[
    path('',views.cart_detail,name='cart_detail'),
    path('<int:med_id>',views.addcart,name='add_to_cart'),
    path('<int:del_id>/',views.delete_all,name='delete_all'),
    path('<int:med_id>/<int:cart_id>/',views.remove,name='remove'),
    path('add_req/<int:u_slug>/',views.add_req,name='add_req'),
    path('request/',views.request,name='request'),
    path('accept/<int:req_id>/',views.accept,name='accept'),
    path('decline/<int:req_id>/',views.decline,name='Decline')

]