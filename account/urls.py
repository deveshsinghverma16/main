from django.urls import path
from . import views

urlpatterns = [
    path('registerUser',views.registerUser,name='registerUser'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('myCart',views.myCart,name='myCart'),
    path('',views.dashboard,name='dashboard'),
    path('addToCart/<int:food_id>',views.addToCart,name='addToCart'),
    path('checkout',views.checkout,name='checkout'),
    path('myOrders',views.myOrders,name='myOrders'),






]
