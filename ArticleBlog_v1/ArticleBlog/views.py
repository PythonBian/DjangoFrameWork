from django.http import HttpResponse #返回http响应
from django.template.loader import get_template #用来加载settings的TEMPLATES配置当中的html页面

def index(request):
    template = get_template("index.html") #加载页面
    result = template.render({"name":"老李"}) #类似字符串的渲染 "%s"%a
    return HttpResponse(result) #返回的内容需要是渲染的结果

# def page_list(request,page):
#     page = int(page) #page来自于url
#     template = get_template("page_list.html") #加载html页面
#     result = template.render({"page":page}) #将url传递进来的page渲染到页面上
#     return HttpResponse(result) #返回渲染的结果

class Saying:
    def say(self):
        return "哈哈哈哈哈"

def template_variable(request):
    data = {
        "name": "老边",
        "en_name": "Old Bian",
        "age": 18,
        "project": ["python","PHP","linux","java","c","c++","c#","Flash","html","易"],
        "score": {"python":100,"PHP":12},
        "s": Saying()
    }
    temp = get_template("template_variable.html")
    result = temp.render(data)
    return HttpResponse(result)


def template_label(request):
    data = {
        "teacher": [
            {"name": "老边", "age": 18},
            {"name": "老张", "age": 23},
            {"name": "老温", "age": 43},
            {"name": "老王", "age": 65},
            {"name": "老申", "age": 48}
        ],
        "outer":"abc",
        "login_valid": 0,
        "commit": "<script>alert('hello world')</script>"
    }

    temp = get_template("template_label.html")
    result = temp.render(data)
    return HttpResponse(result)

# def template_label(request):
#     data = {
#         "name": "老边",
#         "age": 18,
#         "project": ["python","PHP","linux","java","c","c++","c#","Flash","html","易"],
#         "score": {"python":100,"PHP":12},
#     }
#     temp = get_template("template_label.html")
#     result = temp.render(data)
#     return HttpResponse(result)
articles = [
    {"id": 1, "title": "背影", "author": "朱自清", "public_time": "1883-3-3","content": "买橘子的故事","image":"image/by.jpg"},
    {"id": 2, "title": "骆驼祥子", "author": "老舍", "public_time": "1885-3-3", "content": "北京最早的D哥的爱情故事","image":"image/ltxz.jpg"},
    {"id": 3, "title": "鬼吹灯", "author": "三叔", "public_time": "1873-3-3", "content": "空气对流的故事","image":"image/gcd.jpg"},
    {"id": 4, "title": "蜀道难", "author": "李白", "public_time": "1643-3-3", "content": "那是一条神奇的天路","image":"image/adn.jpg"},
    {"id": 5, "title": "道德经", "author": "老子", "public_time": "1873-3-3", "content": "教育的故事","image":"image/ddj.jpg"}
]

def page_list(request):
    template = get_template("page_list.html")
    result = template.render({"articles":articles})
    return HttpResponse(result)

def page(request,id):
    id = int(id)
    article = ""
    for art in articles:
        if art["id"] == id:
            article = art
            break
    template = get_template("page.html")
    result = template.render({"article":article})
    return HttpResponse(result)