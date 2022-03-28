"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    board = [1,2,3,4,5,6,7,8,9]
    return board

def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    print(board[position])
    if board[position-1] == 'o':
        print('not legal')
        return False
    elif board[position-1] == 'x':
        print("not legal")
        return False
    else:
        return True


def fill_spot(board, position, character):

    character = character.strip().lower()
    board[position-1] = character

    print_board(board)


def winning_game(board):
    r_1 = 0
    r_2 = 3



    combination = [1,4,7]
    for i in range(3):

        if board[r_1:r_2] == ['o','o','o']:
            return True
        elif board[r_1:r_2] == ['x','x','x']:
            return True
        else:
            for r in range(len(combination)):
                ''.join(str(combination))
                if combination == "XXX" :
                    print("TRUE")
        r_1 = r_1 + 3
        r_2 = r_2 + 3

def game_over(board):
    for i in board:
        if i == type(int):
            print("going")
        else:
            print("full")



def get_winner(board):
    if winning_game(board):
        xCount = 0
        oCount = 0

        for position in board:
            if position == 'x':
                xCount = xCount + 1
            elif position == 'o':
                oCount = oCount + 1

        if xCount == oCount:
            print("O Won")
            #game_over(board)
            return 'o'
        else:
            print("X Won")
            #game_over(board)
            return 'x'
    else:
        return None


def play(board):
    print_board(board)
    while not get_winner(board):
        x_position = eval(input("x's choose a position:\n"))
        if is_legal(board, x_position):
            fill_spot(board, x_position, 'x')
        else:
            play(board)

        if winning_game(board):
            get_winner(board)
            answer = input("Game is over, hit y to play again")
            if answer == "y":
                play(build_board())


        o_position = eval(input("o's choose a position:\n"))
        if is_legal(board, o_position):
            fill_spot(board, o_position, 'o')
        else:
            play(board)


        if winning_game(board):
            get_winner(board)
            answer = input("Game is over, hit y to play again")
            if answer == "y":
                play(build_board())

def main():
    play(build_board())


if __name__ == '__main__':
    main()
