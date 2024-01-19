from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('menu/',menu,name='menu'),
    path('products/',products,name='products'),
    path('review/',review,name='review'),
    path('contact/',contact,name='contact'),
    path('blogs/',blogs,name='blogs'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('savedata/',savedata,name='savedata'),
    path('logindata/',logindata,name='logindata'),
    path('logout/',logout,name='logout')
]