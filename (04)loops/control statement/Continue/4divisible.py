#Print even numbers between 1 to 20 skip multiples of 4.

for x in range(1,21):
    if x%2==0:
        if x%4 == 0:
            continue
        print(x)