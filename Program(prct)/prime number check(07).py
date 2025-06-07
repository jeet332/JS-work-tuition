n=int(input("Enter a number: "))
flag =0
if n>1:
    for a in range(2,n):
        if n % a ==0:
            flag =1
            break

    if flag ==1:
         print("not prime.")
    else:
         print("prime")

