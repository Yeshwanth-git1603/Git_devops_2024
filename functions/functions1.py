# functions 

## with arguments with return type
# with arguments no return type
# without arguments with return type
# without arguments without return type

def add(x,y):
    z=x+y
    return z
    
a=add(10,20)
print(a)

def mul(x,y):
    z=x*y
    print(z)
    
mul(10,20)

def sub():
    x=int(input("enter the num"))
    y=int(input("enter the num"))
    z=x-y
    return z
    
s=sub()
print(s)


def div():
    print("without arguments without return type")
    x=1
    y=2
    z=x/y
    print(z)
    
div()

# area of rectangle
## with arguments with return type
# with arguments no return type
# without arguments with return type
# without arguments without return type

def ar(l,b):
    res=l*b
    return res
    
r=ar(1,2)
print("area of rectangle is",r)

def ar(l,b):
    res=l*b
    print("area of rectangle is",res)
    
a=ar(10,20)
print(a)


def ar():
    l=int(input("enter the lenght"))
    b=int(input("enter the breadth"))
    res=l*b
    return res
    
b=ar()
print(b)


def ar():
       l=int(input("enter the lenght"))
       b=int(input("enter the breadth"))
       res=l*b
       print("area of rectangle is",res)
       
ar()