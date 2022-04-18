from random import randint

def find_and_remove_first(list, value):
    index = -1
    if value in list:
        while list[index] != value:
            index += 1
            if list[index] == value:
                list.remove(list[index])
                list.insert(index, 'Andreas D.')
                print(list)
                return list


def good_input():
    user_input = 0
    while user_input not in range(1,11):
        user_input = eval(input("Enter a number between 1-10:\n"))
        if user_input in range(1,11):
            break
        else:
            print("Error: Number not in range")
    print("Good input")

def num_digits():
    user_input = eval(input("Enter a positive number:\n"))
    div_amount = 0
    if user_input > 0:
        while user_input != 0:
            div_amount += 1
            user_input = user_input // 10
        print(div_amount)
    else:
        print("Not a positive number")

def hi_lo_game():
    number = randint(1,100)
    guesses = 7
    while guesses != 0:
        user_input = eval(input("Guess a number between 1-100:\n"))
        if user_input == number:
            print("correct")
            print("You win in",8 - guesses,"guesses!")
            quit()
        elif user_input > number:
            print("too high")
            guesses -= 1
        else:
            print("too low")
            guesses -= 1
    print("Sorry, you lose. The number was",number)
l = [3,7,2,7,9,8,4,5]
find_and_remove_first(l, 3)
good_input()
num_digits()
hi_lo_game()