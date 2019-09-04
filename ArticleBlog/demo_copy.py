import copy

# 浅
# lst=[1,2,3,[4,5]]
# lst2=lst.copy()
# print(id(lst))
# print(id(lst2))
# print("----------")
# print(id(lst[3]))
# print(id(lst2[3]))
# lst[3].append(6)
# print(lst)
# print(lst2)


#
lst=[1,2,3,[4,5]]
lst2=copy.deepcopy(lst)
print(lst)
print(lst2)
# print("------------")
# print(id(lst))
# print(id(lst2))
lst[3].remove(4)
print(lst)
print(lst2)
print("------------")

# print(id(lst[2]))
# print(id(lst2[2]))

# print("------------")
# print(id(lst[2]))
# print(id(lst2[2]))
# print("------------")
# a=3
# b=3
# print(id(a))
# print(id(b))