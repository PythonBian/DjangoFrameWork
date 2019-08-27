"""
正则是一种高级的字符串处理方式，通常用于字符的匹配
字符串匹配有两种
    内容配置  re
        通过描述要匹配内容的类型和个数来实现匹配
        匹配手机号
            11位数字
    结构匹配  lxml xpath
        通过描述要匹配内容在整体当中的结构来实现匹配
        匹配手机号
            手机号:后面跟着的东西
"""
import re
#类型匹配
string = "hello\tworld \n I am xiaoming this is 2019 _time_"
    # 原样匹配，匹配对应的原样字符，通常不单独使用，
        #匹配手机号
            #匹配139开头的11位数字
    # .匹配，匹配任意非换行字符
#result = re.findall(r"...",string)#返回所有满足条件的匹配对象
#print(result)
    # \w 匹配所有数字，字母，下划线
#result = re.findall(r"\w",string)#返回所有满足条件的匹配对象
#print(result)
    #\W 匹配所有非数字，非字母，非下划线
#result = re.findall(r"\W",string)#返回所有满足条件的匹配对象
#print(result)
    #\d 匹配数字
#result = re.findall(r"\d\d",string)#返回所有满足条件的匹配对象
#print(result)
    #\D 非数字
#result = re.findall(r"\D",string)#返回所有满足条件的匹配对象
#print(result)
    #[] 返回中括号当中的任意一个字符
# result = re.findall(r"[hl]",string)#返回所有满足条件的匹配对象
# print(result)
    # [] 返回中括号当中的范围任意一个字符
# result = re.findall(r"[a-zA-Z0-9]",string)#返回所有满足条件的匹配对象
# print(result)
    # [] 返回非中括号当中的任意一个字符
# result = re.findall(r"[^a-zA-Z0-9]",string)#返回所有满足条件的匹配对象
# print(result)
    # | 匹配两边任意一边的字符
# result = re.findall(r"h|l",string)#返回所有满足条件的匹配对象
# print(result)
# result = re.findall(r"[hl]",string)#返回所有满足条件的匹配对象
# print(result)
#
# result = re.findall(r"he|lo|as|cs|ss|12",string)#返回所有满足条件的匹配对象
# print(result)
# result = re.findall(r"[helo]",string)#返回所有满足条件的匹配对象
# print(result)
    # () 组匹配,就是将组外的匹配作为条件匹配
#result = re.findall(r"h\w",string)#匹配h后面跟着数字或者字母或者下划线的字符串
#print(result)
#result = re.findall(r"h(\w)",string)#匹配一个数字或者字母或者下划线，这个字母前面需要时h
#print(result)
    # () 命名组匹配,给组起名字，然后调用
# string = "123 323 666 878"
# result = re.findall(r"(\d)\d",string)#匹配h后面跟着数字或者字母或者下划线的字符串
# print(result)
# #id = \d匹配的结果
# result = re.findall(r"(?P<aa>\d)\d(?P=aa)",string)#匹配一个数字或者字母或者下划线，这个字母前面需要时h
# print(result)
#长度匹配
    # *匹配 0到多次
# result = re.findall(r"\d*",string)
# print(result)
    # + 匹配 1到多次
# result = re.findall(r"\d+",string)
# print(result)
    # ? 匹配 0到1次
# result = re.findall(r"\d?",string)
# print(result)
    #{} 匹配指定次
# result = re.findall(r"\d{3}",string) #匹配3个
# print(result)
#
# result = re.findall(r"\d{1,2}",string) #最好匹配2个，匹配1个也行
# print(result)

#特殊匹配
    #^ 匹配开头
# result = re.findall(r"^\w{1,2}",string) #最好匹配2个，匹配1个也行
# print(result)
    #$ 匹配结尾
# result = re.findall(r"\w{1,2}$",string) #最好匹配2个，匹配1个也行
# print(result)
string = "hello wolrd"
string = "hello wolrd"

result = re.findall("(?P<hello>\w)",string)

print(result)
