
def outer(fun):
    def inner(a,b,c,d):
        print("this is inner")
        fun(a,b,c,d)
        print("inner is end")
    return inner

@outer #hello = outer(hello) a = a+1
def hello(a,b,c,d):
    print("I am hello")
@outer #hi = outer(hi)
def hi(a,b,c,d):
    print("i am hi")

hello(1,2,3,4)

#h = outer(hello)()
#h = outer(hello)
#h()
#hello = outer(hello)
#hello()
