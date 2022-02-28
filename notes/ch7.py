import math

def Converter():
    Temp = eval(input("Enter the temp: "))
    T = Temp * 9/5+32
    if T > 90:
        print("Its hot in here")
    else:
        print("Its cold in here")
#Converter()

def quadtradic(a,b,c):

    root_1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
    root_2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
    print(root_1)
    print(root_2)

quadtradic(1,10,3)