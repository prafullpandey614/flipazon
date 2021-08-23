from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('',views.index,name='home'),
   path('contact',views.contact,name='contact'),
   path('home',views.index,name='home'),
   path('checkout',views.checkout,name='checkout'),
   path('sale',views.sale,name='sale'),
   path('offers',views.offers,name='offers'),
   path('phone',views.phone,name='phones'),
   path('womenoffer',views.womenoffer,name='phones'),
   path('login',views.login,name='login')
]
