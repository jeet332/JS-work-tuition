first=0
second = 1
counter=0
n=int(input("Enter your number: "))
if n<=0:
    print("Enter a positive interger.")
else:
    while counter<n:
        print(first, end=" ")
        tem=first+second
        first=second
        second=tem
        counter=counter+1