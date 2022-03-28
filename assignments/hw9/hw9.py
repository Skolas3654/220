from random import randint

def get_words(file_name):
    file = open(file_name, 'r')
    word_list = []
    for line in file:
        word_list.append(line)
    return word_list





def get_random_word(words):
    word = words[randint(1,len(words))]
    return word

a = get_words('words.txt')
print(get_random_word(a))


def letter_in_secret_word(letter, secret_word):
    pass


def already_guessed(letter, guesses):
    pass


def make_hidden_secret(secret_word, guesses):
    pass


def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
