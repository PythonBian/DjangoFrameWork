import hashlib

from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import JsonResponse

from LoginUser.models import *

def loginValid(fun):
    def inner(request,*args,**kwargs):
        cookie_username = request.COOKIES.get("username")
        session_username = request.session.get("username")
        if cookie_username and session_username and cookie_username == session_username:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

def register(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email:
            #首先检测email有没有
            user = LoginUser.objects.filter(email = email).first()
            if not user:
                new_user = LoginUser()
                new_user.email = email
                new_user.username = email
                new_user.password = setPassword(password)
                new_user.save()
            else:
                error_message = "邮箱已经被注册，请登录"
        else:
            error_message = "邮箱不可以为空"
    return render(request,"register.html",locals())

def login(request):
    error_message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email:
            # 首先检测email有没有
            user = LoginUser.objects.filter(email=email).first()
            if user:
                db_password = user.password
                password = setPassword(password)
                if db_password == password:
                    response = HttpResponseRedirect("/index/")
                    response.set_cookie("username",user.username)
                    response.set_cookie("user_id", user.id)
                    request.session["username"] = user.username
                    return response
                else:
                    error_message = "密码错误"
            else:
                error_message = "用户名不存在"
        else:
            error_message = "邮箱不可以空"
    return render(request,"login.html",locals())

def logout(request):
    response = HttpResponseRedirect("/login/")
    keys = request.COOKIES.keys()
    for key in keys:
        response.delete_cookie(key)
    del request.session["username"]
    return response

@loginValid
def index(request):
    return render(request,"index.html",locals())

@loginValid
def goods_list(request,status,page=1):
    page = int(page)
    if status == "1":
        goodses = Goods.objects.filter(goods_status = 1)
    elif status == "0":
        goodses = Goods.objects.filter(goods_status = 0)
    else:
        goodses = Goods.objects.all()
    all_goods = Paginator(goodses,10)
    goods_list = all_goods.page(page)
    return render(request,"vue_goods_list.html",locals())
@loginValid
def goods_status(request,state,id):
    id = int(id)
    goods = Goods.objects.get(id = id)
    if state == "up":
        goods.goods_status = 1
    elif state == "down":
        goods.goods_status = 0
    goods.save()
    url = request.META.get("HTTP_REFERER","/goods_list/1/1")
    return HttpResponseRedirect(url)

@loginValid
def personal_info(request):
    user_id = request.COOKIES.get("user_id")
    user = LoginUser.objects.get(id = int(user_id))
    if request.method == "POST":
        user.username = request.POST.get("username")
        user.gender = request.POST.get("gender")
        user.age = request.POST.get("age")
        user.phone_number = request.POST.get("phone_number")
        user.address = request.POST.get("address")
        user.photo = request.FILES.get("photo")
        user.save()
    return render(request,"personal_info.html",locals())







def goods_list_api(request,status,page=1):
    page = int(page)
    if status == "1":
        goodses = Goods.objects.filter(goods_status = 1)
    elif status == "0":
        goodses = Goods.objects.filter(goods_status = 0)
    else:
        goodses = Goods.objects.all()
    all_goods = Paginator(goodses,10)
    goods_list = all_goods.page(page)

    res = []
    for g in goods_list:
        res.append({
            "goods_number": g.goods_number,
            "goods_name": g.goods_name,
            "goods_price": g.goods_price,
            "goods_count": g.goods_count,
            "goods_location": g.goods_location,
            "goods_safe_date": g.goods_safe_date,
            "goods_pro_time": g.goods_pro_time,
            "goods_status": g.goods_status
        })
    result = {
        "data": res,
        "page_range": list(all_goods.page_range),
        "page":"page"
    }
    return JsonResponse(result)
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
#https://getman.cn/

class GoodsView(View):
    """
    可以自定义http所有的请求的方法的处理
     http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs) #保证父类的init正常运行
        self.result = {
            "version": "1.0",
            "code": 200, #按照http状态码
            "data":""
        }#定义一个规范的返回格式
        self.obj = Goods
    def get(self,request):
        """
            当前方法用于处理get请求
            如果传递id,就返回对应id的数据
            如果不传递就返回所有数据
        """
        id = request.GET.get("id")
        if id:
            result = self.obj.objects.get(id = int(id))
            data = {
                    "goods_number":result.goods_number,
                    "goods_name": result.goods_name,
                    "goods_price": result.goods_price,
                    "goods_count": result.goods_count,
                    "goods_location": result.goods_location,
                    "goods_safe_date": result.goods_safe_date,
                    "goods_pro_time": result.goods_pro_time,
                    }
        else:
            result = self.obj.objects.all()
            data = []
            for res in result:
                data.append(
                    {
                        "goods_number": res.goods_number,
                        "goods_name": res.goods_name,
                        "goods_price": res.goods_price,
                        "goods_count": res.goods_count,
                        "goods_location": res.goods_location,
                        "goods_safe_date": res.goods_safe_date,
                        "goods_pro_time": res.goods_pro_time,
                    }
                )
        self.result["data"] = data
        return JsonResponse(self.result)

    def post(self,request):
        """
        当前方法用于处理post请求
        用来保存数据
        """
        goods = self.obj()
        goods.goods_number = request.POST.get("goods_number")
        goods.goods_name = request.POST.get("goods_name")
        goods.goods_price = request.POST.get("goods_price")
        goods.goods_count = request.POST.get("goods_count")
        goods.goods_location = request.POST.get("goods_location")
        goods.goods_safe_date = request.POST.get("goods_safe_date")
        goods.goods_pro_time = request.POST.get("goods_pro_time")
        goods.goods_status = 1
        goods.save()
        self.result["data"] = {
            "id":goods.id,
            "name":goods.goods_name,
            "data":"save success"
        }
        return JsonResponse(self.result)

    def put(self,request):
        "当前方法用于处理put请求"
        print(request.body)
        put = json.loads(request.body.decode()) #json.loads不能解字节 b''
        id = put.get("id")
        goods_number = put.get("goods_number")
        goods = self.obj.objects.get(id = id)
        goods.goods_number = goods_number
        goods.save()
        self.result["data"] = {
            "id": goods.id,
            "name": goods.goods_name,
            "data": "change success"
        }
        return JsonResponse(self.result["data"])

    def delete(self,request):
        "当前方法用于处理delete请求"
        print(request.body)
        delete = json.loads(request.body.decode())  # json.loads不能解字节 b''
        id = delete.get("id")
        self.obj.objects.get(id = id).delete()
        self.result["data"] = {
            "id": id,
            "data": "delete success"
        }
        return JsonResponse({"methods": "delete", "state": "success"})

from rest_framework import viewsets,mixins
from LoginUser.serializer import *

# class GoodsViewSet(viewsets.ModelViewSet):
#     queryset = Goods.objects.all() #接口数据的源
#     serializer_class = GoodsSerializer
class GoodsViewSet(mixins.CreateModelMixin, #创建的接口方法
                   mixins.RetrieveModelMixin, #查询部分方法
                   mixins.UpdateModelMixin, #修改的方法
                   mixins.DestroyModelMixin, #删除的方法
                   mixins.ListModelMixin, #展示的方法
                   viewsets.GenericViewSet):
    queryset = Goods.objects.all() #接口数据的源
    serializer_class = GoodsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = LoginUser.objects.all()  # 接口数据的源
    serializer_class = UserSerializer


import random

def add_goods(request):
    goods_name = "菠菜、甜菜、芹菜、胡萝卜、小茴香、芫荽、番茄、茄子、辣椒、黄瓜、西葫芦、南瓜、芜菁、白菜、甘蓝、芥菜四季豆 豌豆 胡豆 毛豆 土豆 黄豆芽 绿豆芽、豆芽 甘蓝菜 包心菜; 大白菜 小白菜 水白菜 西洋菜 通心菜 潺菜 花椰菜 西兰花 空心菜 金针菜 芥菜 芹菜 蒿菜 甜菜 紫菜 生菜 菠菜 韭菜 香菜 发菜 榨菜 雪里红 莴苣 芦笋 竹笋 笋干 韭黄 白萝卜 胡萝卜 荸荠 菜瓜 丝瓜 水瓜 南瓜 苦瓜 黄瓜 青瓜 付子瓜 冬瓜".replace(" ","、")
    goods_name = goods_name.split("、")
    goods_address = "河北省，山西省，辽宁省，吉林省，黑龙江省，江苏省，浙江省，安徽省，福建省，江西省，山东省，河南省，湖北省，湖南省，广东省，海南省，四川省，贵州省，云南省，陕西省，甘肃省，青海省，台湾省".split("，")
    for j,i in enumerate(range(100),1):
        goods = Goods()
        goods.goods_number = str(j).zfill(5)
        goods.goods_name = random.choice(goods_address)+random.choice(goods_name)
        goods.goods_price = random.random()*100
        goods.goods_count = random.randint(30,100)
        goods.goods_location = random.choice(goods_address)
        goods.goods_safe_date = random.randint(1,36)
        goods.save()
    return HttpResponse("hello world")
# Create your views here.
