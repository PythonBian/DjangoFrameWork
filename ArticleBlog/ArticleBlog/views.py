from django.http import HttpResponse

def index(request):
    """
    :param request: 在django的视图函数当中，起到接受请求的作用
    """
    #django规定，响应必须是一个response对象
    #1+"a"
    return HttpResponse('<h1 style="color:red;">hello world</h1>')
    # return '<h1 style="color:red;">hello world</h1>'
def index1(request):
    """
    :param request: 在django的视图函数当中，起到接受请求的作用
    """
    #django规定，响应必须是一个response对象
    #1+"a"
    return HttpResponse('<h1 style="color:red;">hello world 1</h1>')
    # return '<h1 style="color:red;">hello world</h1>'

def introduce(request,name,age):
    return HttpResponse('<h1 style="color:red;">hello world,I am %s,I am %s years old</h1>'%(name,age))
