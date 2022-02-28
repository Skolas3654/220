#list = ["1","2","3","4","5","   "]
#st = "1 2 3 4 5"


#for i in range(100):
#    print(list[i%6])
import random
#months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
months = ["Jan","Feb"]

#a = "hello world"
#a = "-|-".join(months)
#print(a)

#print(months)

def User():
    first_name = input("Enter your first name\n")
    last_name = input("Enter your last name\n")
    first_initial = first_name[0]
    last_initial = last_name[0:7]
    username = first_initial + last_initial
    print("Your initials:", username)

def mon():
    month_index = eval(input("Enter a month:\n")) - 1
    print(months[month_index])
    #print(months[month_index * 3:month_index * 3 + 3])

def encode():
    nums = []
    word = input("Enter a word\n")
    for letter in word:
        num = ord(letter)
        nums.append(num)
    print(nums)

def decode():
    unicode = input("Enter numbers\n")
    result = unicode.split()
    for i in result:
        r = chr(int(i))
        print(r, end="")



print("My name is {:-<10} and I am {} years old".format("Bill", 7))

money = 12.50

print("I have ${:.2f}".format(money))

file = "test"
test_file = open(file,'r')
print(test_file.readline()[:-1])

output_file = open("output.txt",'w')

print(test_file, file=output_file)
