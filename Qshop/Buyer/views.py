from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Seller.models import *
from Seller.views import setPassword

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_user = request.COOKIES.get("username")
        session_user = request.session.get("username")
        if cookie_user and session_user and cookie_user == session_user:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/Buyer/login/")
    return inner

def login(request):
    if request.method == "POST":
        password = request.POST.get("pwd")
        email = request.POST.get("email")
        user = LoginUser.objects.filter(email = email).first()
        if user:
            db_password = user.password
            password = setPassword(password)
            if db_password == password:
                response = HttpResponseRedirect("/Buyer/index/")
                response.set_cookie("username",user.username)
                response.set_cookie("user_id",user.id)
                request.session["username"] = user.username
                return response
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
def logout(request):
    url = request.META.get("HTTP_REFERER", "/Buyer/index/")
    response = HttpResponseRedirect(url)
    for k in request.COOKIES:
        response.delete_cookie(k)
    del request.session["username"]
    return response

def index(request):
    goods_type = GoodsType.objects.all() #获取所有类型
    result = []
    for ty in goods_type:
        # 按照生产日期对对应类型的商品进行排序
        goods = ty.goods_set.order_by("-goods_pro_time")
        if len(goods) >= 4: #进行条件判断
            goods = goods[:4]
            result.append({"type":ty,"goods_list":goods})
    return render(request,"buyer/index.html",locals())

def goods_list(request):
    """
    type 代表请求的类型
        t 按照类型查询
            keywords必须是类型id
        k 按照关键字查询
            keywords可以是任何东西
    keywords 代表请求的关键字
    """
    request_type = request.GET.get("type") #获取请求的类型 t 类型查询 k关键字查询
    keyword = request.GET.get("keywords") #查询的内容 t类型 k为类型id  k类型 k为关键字
    goods_list = [] #返回的结果
    if request_type == "t": #t类型查询
        if keyword:
            id = int(keyword)
            goods_type = GoodsType.objects.get(id = id) #先查询类型
            goods_list = goods_type.goods_set.order_by("-goods_pro_time") #再查询类型对应的商品
    elif request_type == "k":
        if keyword:
            goods_list = Goods.objects.filter(goods_name__contains=keyword).order_by("-goods_pro_time") #模糊查询商品名称含有关键字的商品
    if goods_list: #限定推荐的条数
        lenth = len(goods_list) / 5
        if lenth != int(lenth):
            lenth += 1
        lenth = int(lenth)
        recommend = goods_list[:lenth]
    return render(request,"buyer/goods_list.html",locals())

def goods_detail(request,id):
    goods = Goods.objects.get(id = int(id))
    return render(request,"buyer/detail.html",locals())

@loginValid
def user_center_info(request):
    return render(request,"buyer/user_center_info.html",locals())
# Create your views here.

