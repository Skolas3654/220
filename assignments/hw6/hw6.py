"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description
of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import math

def cash_converter():
    value = eval(input("Enter an integer:\n"))
    print("That is ${:.2f}".format(value))

#cash_converter()

def encode():
    encoded_message = []
    message = input("Enter a message:")
    key = eval(input("Enter a key:"))

    for i in message:
        encoder = ord(i) + key
        encoder = chr(encoder)
        encoded_message.append(encoder)
    encoded_message = "".join(encoded_message)
    print(encoded_message)
#encode()


def sphere_area(radius):
    sphere_a = 4 * math.pi * radius ** 2
    return sphere_a

#a = sphere_area(4)
#print(a)

def sphere_volume(radius):
    sphere_v = (4/3) * math.pi * radius ** 3
    return sphere_v

#b = sphere_volume(7)
#print(b)

def sum_n(number):
    sqr_res = 0
    for _ in range(1, number+1):
        sqr_res = (number * (number + 1) * (2 * number + 1)) / 6

    return sqr_res
#print(sum_n(26))

def sum_n_cubes(number):
    cube_res = 0
    for i in range(1, number+1):
        cube_res +=i*i*i
    return cube_res


def encode_better():
    message = input("Enter a message")
    key = input("Enter a key")
    #message = "dolphin"
    #key = "ace"
    encoded_message = []

    for i in range(len(message)):


        key_ord_value = ord(key[i % len(key)])

        key_ord_value = key_ord_value

        message_ord_value = ord(message[i])
        letter_chr = key_ord_value + message_ord_value
        letter_chr = chr(letter_chr)

        encoded_message.append(letter_chr)


    secret_code = "".join(encoded_message)
    print(secret_code)


#encode_better()
if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
