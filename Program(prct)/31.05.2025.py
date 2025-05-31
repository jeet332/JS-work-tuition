# write a program to calculate the factorial number using function.





n = int(input("Enter the number: "))
def function(n):

    fact=1
    while (n > 0):
        fact = fact*n
        n-=1
    return fact
print("factorial","=",function(n))