from django.contrib import admin
from django.urls import path
#from app_store.views import Index #, store
from app_store.views import Signup
from app_store.views import logout, Login
from app_store.views import Cart
from app_store.views import CheckOut
from app_store.views import OrderView
from app_store.middlewares.auth import  auth_middleware
from .views import StoreView # AnohLoginView


urlpatterns = [
    #path('', Index.as_view(), name='homepage'),
    #path('store', store, name='store'),
    path('', StoreView.as_view(), name='store'),
    path('signup', Signup.as_view(), name='signup'),
    #path('login', AnohLoginView.as_view(), name='login'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]