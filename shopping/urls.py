from django.contrib import admin
from django.urls import path
from .views import  *
#   home ,add_to_cart, view_cart, remove_from_cart,update_quantity,minus_quantity,checkout,buy_now,download_invoice,save_shipping_details

urlpatterns = [
    path('',home,name="home"),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:cart_item_id>/', update_quantity, name='update_quantity'),
    path('cart/minus/<int:cart_item_id>/', minus_quantity, name='minus_quantity'),
    path('checkout/', checkout, name='checkout'),
    path('buy-now/<int:product_id>/', buy_now, name='buy_now'),
    path('download-invoice/', download_invoice, name='download_invoice'),
    path('download-invoice/<int:order_id>/', download_invoice, name='download_invoice'),

    
    path('save-shipping/',save_shipping_details, name='save_shipping'),
    path('signup/', signup_view, name='signup'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

    


     

]


