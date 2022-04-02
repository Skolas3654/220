from random import randint
from graphics import GraphWin, Line, Point, Circle, Entry, Text

def get_words(file_name):
    file = open(file_name, 'r')
    word_list = []
    for line in file:
        word_list.append(line)
    return word_list


def get_random_word(words):
    list_length = len(words)-1
    word = words[randint(0,list_length)]

    return word.replace('\n','')



def letter_in_secret_word(letter, secret_word):
    for i in secret_word:
        if i == letter:
            return True
    return False

def already_guessed(letter, guesses):
    for i in guesses:
        if i == letter:
            return True
    return False


def make_hidden_secret(secret_word, guesses):

    for i in range(len(secret_word)):
        if secret_word[i] not in guesses:
            secret_word = secret_word.replace(secret_word[i], "_")
    secret_word = secret_word.replace(""," ")[1: -1]
    return secret_word


def won(guessed):
    guessed = guessed.replace(" ","")
    for i in guessed:
        if i == "_":
            return False

    return True

def draw_hangman(remaining_guesses, win):
    head = Circle(Point(250,100),25)
    torso = Line(Point(270,115),Point(270,220))
    arm_1 = Line(Point(270,125),Point(255,190))
    arm_2 = Line(Point(270, 125), Point(264,190))
    leg_1 = Line(Point(270,215),Point(260,270))
    leg_2 = Line(Point(270, 215), Point(270, 275))

    if remaining_guesses == 5:
        head.draw(win)
    if remaining_guesses == 4:
        torso.draw(win)
    if remaining_guesses == 3:
        arm_1.draw(win)
    if remaining_guesses == 2:
        arm_2.draw(win)
    if remaining_guesses == 1:
        leg_1.draw(win)
    if remaining_guesses == 0:
        leg_2.draw(win)

def play_graphics(secret_word):
    height = 500
    width = 500
    win = GraphWin("Hangman", width, height)

    word_list = get_words('words.txt')
    secret_word = get_random_word(word_list)

    entry_box_text = Text(Point(width/4,350),'Guess a letter: ')
    entry_box = Entry(Point(width/2,350),10)

    guessed_letters = []
    remaining_guesses = 6

    display_word = make_hidden_secret(secret_word, guessed_letters)
    display_word_text = Text(Point(width / 2,300), display_word)

    guesses = make_hidden_secret(secret_word, guessed_letters)

    guesses_text = Text(Point(width / 2,420), guessed_letters)
    pre_guesses_text = Text(Point(width / 2,400), "Letters already used:")

    entry_box_text.draw(win)
    entry_box.draw(win)
    display_word_text.draw(win)
    guesses_text.draw(win)
    pre_guesses_text.draw(win)

    while not won(guesses) and remaining_guesses > 0:
        win.getMouse()
        player_guess = entry_box.getText()

        if already_guessed(player_guess, guessed_letters):
            entry_box.setText("")

        elif letter_in_secret_word(player_guess, secret_word):
            guessed_letters.append(player_guess)
            display_word_text.setText(make_hidden_secret(secret_word, guessed_letters))
            guesses = make_hidden_secret(secret_word, guessed_letters)
            guesses_text.setText(guessed_letters)
            entry_box.setText("")
        else:
            guessed_letters.append(player_guess)
            guesses = make_hidden_secret(secret_word, guessed_letters)
            guesses_text.setText(guessed_letters)
            remaining_guesses -= 1
            draw_hangman(remaining_guesses, win)
            entry_box.setText("")
    entry_box.undraw()
    pre_guesses_text.undraw()
    entry_box_text.undraw()

    if won(guesses):
        guesses_text.setText("YOU WON, NICE JOB")
    else:
        guesses_text.setText("YOU LOST")

    close_text = Text(Point(250,450),"Click to close!")
    close_text.draw(win)

    win.getMouse()



#play_graphics('')



def play_command_line(secret_word):

    guessed_letters = []
    remaining_guesses = 6
    display_word = make_hidden_secret(secret_word, guessed_letters)

    guesses = make_hidden_secret(secret_word, guessed_letters)

    while not won(guesses) and remaining_guesses > 0:

        print("already guessed:",guessed_letters)
        print("guesses remaining:",remaining_guesses)
        print(display_word)

        player_guess = input("guess a letter: \n")[0]

        if already_guessed(player_guess, guessed_letters):
            pass

        elif letter_in_secret_word(player_guess, secret_word):
            guessed_letters.append(player_guess)
            display_word = make_hidden_secret(secret_word, guessed_letters)
            guesses = make_hidden_secret(secret_word, guessed_letters)
        else:
            guessed_letters.append(player_guess)
            guesses = make_hidden_secret(secret_word, guessed_letters)
            remaining_guesses -= 1


#play_command_line('apple')

if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
