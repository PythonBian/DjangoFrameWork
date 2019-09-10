from django.http import HttpResponseRedirect
from django.shortcuts import render
from Seller.models import *
from Seller.views import setPassword

def login(request):
    if request.method == "POST":
        password = request.POST.get("pwd")
        email = request.POST.get("email")
        user = LoginUser.objects.filter(email = email).first()
        if user:
            db_password = user.password
            password = setPassword(password)
            if db_password == password:
                return HttpResponseRedirect("/Buyer/index/")
    return render(request, "buyer/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("pwd")
        email = request.POST.get("email")

        user = LoginUser()
        user.username = username
        user.password = setPassword(password)
        user.email = email
        user.save()
        return HttpResponseRedirect("/Buyer/login/")
    return render(request, "buyer/register.html")

def index(request):
    goods_type = GoodsType.objects.all()
    result = []
    for ty in goods_type:
        goods = ty.goods_set.order_by("-goods_pro_time")
        if len(goods) >= 4:
            goods = goods[:4]
            result.append({"type":ty,"goods_list":goods})
    return render(request,"buyer/index.html",locals())

def logout(request):
    return render(request,"buyer/index.html")


# Create your views here.

