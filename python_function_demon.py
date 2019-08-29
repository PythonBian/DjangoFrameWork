# 
# def inner(start,end):
#     return "hello world"[start:end]
# inner(1,2)
# 
# #惰性
# def outer(start,end):
#     def inner():
#         return "hello world"[start:end]
#     return inner
# outer(1,2)
# 

# 
# import pymysql
# 
# connect = pymysql.connect(
#     host = "localhost",
#     user = "root",
#     password = "111111",
#     database = "student"
# )
# 
# cursor = connect.cursor()
# 
# sql = "select name from stu"
# 
# result = cursor.execute(sql)
# 
# for data in cursor.fetchall():
#     print(data)
# 
# connect.commit()
# cursor.close()
# connect.close()



example = {"a":1}

print(example.get("b","没有了"))


