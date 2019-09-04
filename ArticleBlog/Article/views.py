from django.shortcuts import render_to_response #=get_template+HttpResponse
from django.core.paginator import Paginator
from Article.models import *

def set_page(page_list,page):
    """
    page_list  # 页码范围
    page #页码
    想要当前页码的前两页和后两页
    """
    if page - 3 < 0:
        start = 0
    else:
        start = page - 3
    if page+2 > 49:
        end = 49
    else:
        end = page+2
    return list(page_list[start:end])


def newList(request,types,p):
    p = int(p)
    page_size = 6
    articles = ArticleType.objects.get(label=types).article_set.order_by("-public_time")
    # articles = Article.objects.filter().order_by("-public_time")
    article_list = Paginator(articles,page_size) #进行分页
    page_article= article_list.page(p) #返回对应页的数据
    page_range = set_page(article_list.page_range,p) #返回对应页的页码
    return render_to_response("newlist.html",locals())

def new(request,id):
    """
    半新版本
    """
    article = Article.objects.get(id = id)
    # article_list = Article.objects.filter(title="背影").first()
    # article_list = Article.objects.filter(title="背影").last()

    return render_to_response("new.html",locals())

def index(request):
    """
    1、查询最新的6条
    2、查询推荐7条
    3、查询排行榜点击率前12
    """
    new_article = Article.objects.order_by("-public_time")[:6]
    recom_article = Article.objects.filter(recommend=1).order_by("-public_time")[:7]
    click_article = Article.objects.order_by("-click")[:12]

    return render_to_response("index.html",locals())


def req_arg(request):
    request_method = dir(request)
    return render_to_response("request_arguement.html",locals())

from django.shortcuts import render
def form_exam(request):
    searchKey = request.GET.get("searchKey")
    articles = []
    if searchKey: #判断searchKey是否为真 非空（字符串，字典，列表，元组，set），非0，
        articles = Article.objects.filter(title__contains=searchKey)
    return render(request,"formExample.html",locals())

def csrf_exam(request):
    return render_to_response("csrf_example.html")
import hashlib

def setPassword(password):
    md5 = hashlib.md5() #创建hash md5加密的实例
    md5.update(password.encode()) #进行加密
    result = md5.hexdigest()
    return result

from Article.forms import Register


def register(request):
    register_form = Register()
    if request.method == "POST": #判断请求方式
        # request_data = request.POST
        # data_valid = Register(request_data)
        data_valid = Register(request.POST)
        if data_valid.is_valid(): #判断提交的数据是否合法，如果合法为True，否则为false。
            clean_data = data_valid.cleaned_data #校验过的数据组成的字典
            username = clean_data.get("username")
            password = clean_data.get("password")
            email = clean_data.get("email")
            u = User() #实例化模型
            u.username = username #保存用户名
            u.password = setPassword(password) #保存密码
            u.email = email
            u.save() #保存数据
        else:
            errors = data_valid.errors
            print(errors)
    return render(request,"register.html",locals())

def user_valid(request):
    email = request.GET.get("email") #获取请求的email
    result = {"code":"400","data":""} #定义返回的数据格式
    if email:
        user = User.objects.filter(email = email).first() #安装email查询用户
        if user: #用户存在，邮箱不可用
            result["data"] = "当前邮箱已经完成注册，请登录"
        else: #用户不存在，邮箱可以用
            result["code"] = "200"
            result["data"] = "当前邮箱可以注册"
    else: #空
        result["data"] = "邮箱不可以为空"
    return JsonResponse(result)

def jq_exam(request):
    return render(request,"jqExample.html")

def ajax_get_page(request):
    """
    负责页面
    :param request:
    :return:
    """
    return render(request,"ajax_get_page.html")

from django.http import JsonResponse
def ajax_get_data(request):
    """
    负责数据
    :param request:
    :return:
    """
    name = request.GET.get("name")
    return JsonResponse({"hello":"来自后台的数据,你的名字是%s"%name})

def ajax_post_page(request):
    """
    负责页面
    :param request:
    :return:
    """
    return render(request,"ajax_post_page.html")

from django.http import JsonResponse
def ajax_post_data(request):
    """
    负责数据
    :param request:
    :return:
    """
    return JsonResponse({"hello":"来自后台的数据"})

# def register(request):
#     register_form = Register()
#     if request.method == "POST": #判断请求方式
#         username = request.POST.get("username")  #获取用户名
#         password = request.POST.get("password")  #获取密码
#         if username and password: #判断用户名和密码
#             u = User() #实例化模型
#             u.username = username #保存用户名
#             u.password = setPassword(password) #保存密码
#             u.save() #保存数据
#     return render(request,"register.html",locals())

from django.http import HttpResponseRedirect #跳转
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username = username).first()
        if user:
            db_password = user.password
            password = setPassword(password)
            if password == db_password:
                response = HttpResponseRedirect("/index/")
                response.set_cookie("name","laobian")
                response.set_cookie("age", "18")
                return response #这里写路由不写页面
    return render(request,"login.html")





