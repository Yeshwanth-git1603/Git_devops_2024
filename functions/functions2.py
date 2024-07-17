def fact(x=int(input("enter x"))):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
        
res=fact()
print(res)

for x in range(10):
    print(x*"x")
    
# variable length arguemnts

def var(*args):
    s=0
    for x in args:
        s=s+x
    return s
    
v=var(10,20,30,40,50)
print("the value of v is",v)


# variable length keyword arguments

def var_key(**args):
    print(args)
        
var_key(name="yeshwanth",age=23,college="aits")
