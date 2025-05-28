import math

def HCF(a, b):
    return math.gcd(a, b)


num1 = int(input("Enter a fist number: "))
num2 = int(input("Enter a second number: "))

hcf = HCF(num1, num2)

print({num1},'aur',{num2},'ka HCF hai:',{hcf})
