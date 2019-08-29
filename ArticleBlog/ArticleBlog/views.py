from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response #=get_template+HttpResponse

from Article.models import *
def newList(request):
    """
    底层版本
    """
    #article_list = Article.objects.all() #查询所有数据
    #article_list = Article.objects.filter(title="背影") #按照条件过滤
    #article_list = Article.objects.order_by("-id") #按照条件过滤,通常查询都需要进行排序，order_by相当于排序查询所有
    #article_list = Article.objects.filter(title="背影").order_by("id") # 按照条件过滤,然后排序
    article_list = Article.objects.filter(title="背影").order_by("id").values("title","public_time")
    print(article_list)
    return render_to_response("newlist.html",locals())

def new(request):
    """
    半新版本
    """
    article = Article.objects.get(id = 2)
    article_list = Article.objects.filter(title="背影").first()
    article_list = Article.objects.filter(title="背影").last()

    return render_to_response("new.html",locals())

def index(request):
    """
    当前版本
    """
    username = "laobian"
    return render_to_response("index.html",locals())




