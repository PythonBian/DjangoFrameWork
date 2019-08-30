#import requests
#分页
# count = 5 #每页条数
# def page_random(num):
#     """
#     :param num: 页码
#     :return: 对应页数的页面范围
#     """
#     if num<=45: #num
#         list1 = [] #最后结果的容器
#         if num*count<=25:
#             num = 1
#             for i in range(5):
#                 list1.append(num)
#                 num+=1
#         else:
#             for i in range(5):
#                 list1.append(num)
#                 num+=1
#     else:
#         list1 = "重新输入"
#     return list1
# if __name__ == "__main__":
#     while True:
#         result = page_random(int(input(">>>")))
#         print(result)
#print(page_random(1))


from functools import partial

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

if __name__ == "__main__":
    page_list = range(1,50)
    setPage = partial(set_page,page_list)
    while True:
        page = int(input(">>>"))
        print(setPage(page))


















