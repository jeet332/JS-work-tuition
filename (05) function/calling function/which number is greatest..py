a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
def numbers(a,b,c):
    if(a<b<c):
        print("Third is geater",c)
    elif(c<b<a):
        print("First is greater",a)
    elif(c<a<b):
        print("Second is greater",b)
numbers(a,b,c)