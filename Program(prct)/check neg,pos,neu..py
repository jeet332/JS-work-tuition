n=int(input("Enter a number:"))
def num(n):
    if (n<=-1):
        print("It is a negative.")
    elif(n==0):
        print("It is a neutral number.")
    elif(n>=1):
        print("It is a positive number.")
num(n)