import math


#fact = eval(input("Enter a number\n"))

#for i in range(1,fact):
#    fact = i * fact
#    print(fact)


def root():
    a, b, c = eval(input("Enter a, b, c values:\n"))


    root_1 = (-b + math.sqrt(b * b - 4 * a * c))/2 * a
    root_2 = (-b - math.sqrt(b * b - 4 * a * c))/ 2 * a
    print(root_1)
    print(root_2)

root()
