from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('index/', index),
    path('logout/', logout),
    path('goods_list/', goods_list),
    re_path('goods_detail/(?P<id>\d+)/', goods_detail),
    path('user_info/', user_center_info),
]
