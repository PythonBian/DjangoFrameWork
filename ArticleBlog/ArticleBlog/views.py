from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response #=get_template+HttpResponse

def newList(request):
    """
    底层版本
    """
    template = get_template("newlist.html")
    result = template.render({})
    return HttpResponse(result)

def new(request):
    """
    半新版本
    """
    return render_to_response("new.html",{"a":1})

def index(request):
    """
    当前版本
    """
    username = "laobian"
    return render_to_response("index.html",locals())




