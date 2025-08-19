#User defined Function
#Syntax
'''
def functionName():
    #instructions
'''

def sum():
    print(10+20)

# sum()

def add():
    return 10+20

x = add()
# print(x)

def sub(a=0,b=0):
    print("a is", a)
    print("b is", b)
    return a-b

# y = sub(10,20)
# y = sub(100,20)
# y = sub(1200,210)
# y = sub(1200, 120)
y = sub(b=1200, a=120)
print(y)