from django.shortcuts import render_to_response #=get_template+HttpResponse
from django.core.paginator import Paginator
from Article.models import *

def newList(request):
    p = 1
    page_size = 6
    articles = Article.objects.order_by("-public_time")
    article_list = Paginator(articles,page_size) #进行分页
    page_article= article_list.page(p)
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
    1、查询最新的6条
    2、查询推荐7条
    3、查询排行榜点击率前12
    """
    new_article = Article.objects.order_by("-public_time")[:6]
    recom_article = Article.objects.filter(recommend=1).order_by("-public_time")[:7]
    click_article = Article.objects.order_by("-click")[:12]

    return render_to_response("index.html",locals())




