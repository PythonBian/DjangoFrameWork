from django.http import HttpResponse #返回http响应
from django.template.loader import get_template #用来加载settings的TEMPLATES配置当中的html页面

def index(request):
    template = get_template("index.html") #加载页面
    result = template.render({"name":"老李"}) #类似字符串的渲染 "%s"%a
    return HttpResponse(result) #返回的内容需要是渲染的结果

def page_list(request,page):
    page = int(page) #page来自于url
    template = get_template("page_list.html") #加载html页面
    result = template.render({"page":page}) #将url传递进来的page渲染到页面上
    return HttpResponse(result) #返回渲染的结果