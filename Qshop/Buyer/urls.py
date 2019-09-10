from django.urls import path,include
from Buyer.views import *

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('index/', index),
    path('logout/', logout),
    path('goods_list/', goods_list)
]
