# from module1 import firstmodule as assss
# assss()
#
# #__name__ is a global varible
# print(True if __name__  == "__main__" else False) #True
# print(assss.__name__)   #firstmodule

s=10
def f():
    global s
    print(s)
    s="inside"
    print(s)
f()
