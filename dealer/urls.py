from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin 
urlpatterns=[
    path('',views.home,name='home'),
    path('properties/',views.properties,name='properties'),
    path('contact/',views.contact,name='contact'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('news/',views.news,name='news'),
    path('lahore/',views.lahore,name='lahore'),
    path('karachi/',views.karachi,name='karachi'),
    path('islamabad/',views.islamabad,name='islamabad'),
    path('<int:property_id>/',views.detail,name='detail'),
    path('cart/',views.cart,name='cart'),
    path('login/',views.login,name='login'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart/',views.cart,name='cart'),
]  

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)