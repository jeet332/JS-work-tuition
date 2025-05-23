
# a=int(input("Marks of student: "))
# if (a>= 90):
#     print("A grade")
# elif(a>=80):
#     print("B grade")
# elif(a>=70):
#     print("c grade")
# elif(a>=60):
#     print("d grade")
# else:
#     print("You are fail.")

    # I have done.

A=float(input("Enter your Amount: "))
if(A<=10000):
    bonus=(A*0.05)
    print(bonus)
elif(A<=25000):
    bonus=(A*0.10)
    print(bonus)
elif(A<=50000):
    bonus=(A*0.15)
    print(bonus)
else:
    print("This amount is not listed")