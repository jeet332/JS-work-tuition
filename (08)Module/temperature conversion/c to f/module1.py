def temp(n):
    while(n>0):
        fahrenheit=(n*9/5)+32
        celcius=(fahrenheit-273)
        print(fahrenheit,"fahrenheit")
        print(celcius,"celcius")
        n=float(input("Enter a celcius value: "))