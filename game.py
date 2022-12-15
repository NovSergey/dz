import keyboard
import random
import time
import os
import emoji
points = 0
pole = "⬜"
enemy = "🔺"
player = "🟩"
map_ = [pole]*100
player_coord = random.randint(0, 99)
map_[player_coord] = player



def print_():
    global points
    os.system("cls")
    for i in range(10):
        strk = ""
        for j in range(10*i, 10*(i+1)):
            strk += map_[j]
        print(strk)
    print(points)
    print()
    time.sleep(0.1)

def check():    
    global player_coord, points
    if map_[player_coord] == enemy:
        points += 1

def plus(count):
    global player_coord
    map_[player_coord] = pole
    if count == 10 and player_coord + 10 > 99:
        player_coord = player_coord%10
    elif count == 1 and player_coord == 99:
        player_coord = 0
    else:
        player_coord += count
    check()
    map_[player_coord] = player

def minus(count):
    global player_coord
    map_[player_coord] = pole
    if count == 10 and player_coord - 10 < 0:
        player_coord = 90 + player_coord
    elif count == 1 and player_coord == 0:
        player_coord = 99
    else:
        player_coord -= count
    check()
    map_[player_coord] = player

for i in range(random.randint(5, 10)):
    en_cord = random.randint(0, 99)
    while map_[en_cord] == player and map_[en_cord] == enemy:
        en_cord = random.randint(0, 99)
    map_[en_cord] = enemy
print_()

while True:
    if keyboard.is_pressed("esc"):
        exit()
    elif keyboard.is_pressed('w'):
        minus(10)
        print_()
    elif keyboard.is_pressed('a'):
        minus(1)
        print_()
    elif keyboard.is_pressed('s'):
        plus(10)
        print_()
    elif keyboard.is_pressed('d'):
        plus(1)
        print_()


