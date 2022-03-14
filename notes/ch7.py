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

def first_while():
    i = 0
    while i < 5:
        print(i, end=" ")
        i = i + 1
#first_while()

def is_game_over(player_1_points,player_2_points):
    over_15 = player_1_points >= 15 or player_2_points >= 15
    won_by_two = abs(player_1_points - player_2_points) >= 2
    if over_15 and won_by_two:
        return True
    return False
#print(is_game_over(15,15))

player_1 = 10
player_2 = 12
print(player_1, player_2)
while not is_game_over(player_1,player_2):
    one_points, two_points = eval(input("Enter two points"))
    player_1 = player_1 + one_points
    player_2 = player_2 + two_points
    print(player_1, player_2)
print("Game Over")
