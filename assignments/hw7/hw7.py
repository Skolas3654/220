"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the
problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import encryption
from encryption import encode

def number_words(in_file_name, out_file_name):
    in_file_name = open(in_file_name, 'r')
    out_file_name = open(out_file_name,'w')
    index = 1
    for line in in_file_name:
        for word in line.split():
            print(str(index) + " " + word, file=out_file_name)
            index = index + 1

def hourly_wages(in_file_name, out_file_name):
    in_file_name = open(in_file_name, 'r')
    out_file_name = open(out_file_name, 'w')

    for line in in_file_name:
        employee_info = line.split()
        employee_name = employee_info[0] + " " + employee_info[1]

        employee_pay = (float(employee_info[2]) + 1.65) * int(employee_info[3])
        employee_pay = "{:.2f}".format(employee_pay)

        updated_info = employee_name + " " + str(employee_pay)

        print(updated_info, file=out_file_name)



def calc_check_sum(isbn):


    isbn = isbn.replace("-","")

    result = 0
    mul_index = 10

    for i in isbn:
        i = int(i)

        result = result + i * mul_index
        mul_index = mul_index - 1
    return result





def send_message(file_name, friend_name):
    file_name = open(file_name, 'r')
    friend_name = open(friend_name + ".txt", 'w')

    for i in file_name.readlines():
        print(i, file=friend_name, end="")


def send_safe_message(file_name, friend_name, key):
    file_name = open(file_name, 'r')
    friend_name = open(friend_name + ".txt", 'w')

    for i in file_name.readlines():
        encoded_string = encode(i,key)
        print(encoded_string, file=friend_name)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    pass
