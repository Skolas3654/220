#name, age = eval(input("Enter your name and age\n"))
#print("Hello",name,"you are", age)




balance = eval(input("What is your balance:\n"))
APR = eval(input("What is the APR:\n"))
years = eval(input("How many years would you like to check:\n"))

for var in range(years):
    balance = balance*(APR+1)
    print(balance)
print()


