# patterns 
#right angle triangle

x=int(input("enter the number"))
for i in range(x):
    for j in range(i):
        print("*",end="")
    print()

#right angle triangle

rows = int(input("entre the value"))
i = 1 
while i <=rows :
    j = 1
    while j <= i:
        print(i, end=" ")
        j = j +1
    i = i +1
    print('')

# using while loop downwards

rows = int(input("entre the value"))
i = 1
while i <= rows:
    j = 1

