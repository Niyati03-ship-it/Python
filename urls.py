"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('sindex/',views.sindex,name='sindex'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('shop/',views.shop,name='shop'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('fpass/',views.fpass,name='fpass'),
    path('otp/',views.otp,name='otp'),
    path('newpass/',views.newpass ,name='newpass'),
    path('cpass/',views.cpass ,name='cpass'),
    path('scpass/',views.cpass ,name='scpass'),
    path('uprofile/',views.uprofile,name='uprofile'),
    path('suprofile/',views.uprofile,name='suprofile'),
    path('add/',views.add,name='add'),
    path('view/',views.view,name='view'),
    path('pdetails/<int:pk>',views.pdetails,name='pdetails'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('addwish/<int:pk>',views.addwish,name='addwish'),
    path('wish/',views.wish,name='wish'),
    path('bpdetails/<int:pk>',views.bpdetails,name='bpdetails'),
    path('deletewish/<int:pk>',views.deletewish,name='deletewish'),
    path('addcart/<int:pk>',views.addcart,name='addcart'),
    path('cart/',views.cart,name='cart'),
    path('deletecart/<int:pk>',views.deletecart,name='deletecart'),
    path('sucess/',views.sucess,name='sucess'),
]
