import sys
import traceback

import keyboard
import random
import time
import os
import threading

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow







class MyWindow(QMainWindow):
    def __init__(self):
        global player, enemy, map_, points, check, pole, count_enemys, player_coord
        super().__init__()
        uic.loadUi('design.ui', self)
        check = [self.lb1, self.lb2, self.lb3, self.lb4, self.lb5, self.lb6, self.lb7, self.lb8, self.lb9, self.lb10, self.lb11, self.lb12, self.lb13, self.lb14, self.lb15, self.lb16, self.lb17, self.lb18, self.lb19, self.lb20, self.lb21, self.lb22, self.lb23, self.lb24, self.lb25, self.lb26, self.lb27, self.lb28, self.lb29, self.lb30, self.lb31, self.lb32, self.lb33, self.lb34, self.lb35, self.lb36, self.lb37, self.lb38, self.lb39, self.lb40, self.lb41, self.lb42, self.lb43, self.lb44, self.lb45, self.lb46, self.lb47, self.lb48, self.lb49, self.lb50, self.lb51, self.lb52, self.lb53, self.lb54, self.lb55, self.lb56, self.lb57, self.lb58, self.lb59, self.lb60, self.lb61, self.lb62, self.lb63, self.lb64, self.lb65, self.lb66, self.lb67, self.lb68, self.lb69, self.lb70, self.lb71, self.lb72, self.lb73, self.lb74, self.lb75, self.lb76, self.lb77, self.lb78, self.lb79, self.lb80, self.lb81, self.lb82, self.lb83, self.lb84, self.lb85, self.lb86, self.lb87, self.lb88, self.lb89, self.lb90, self.lb91, self.lb92, self.lb93, self.lb94, self.lb95, self.lb96, self.lb97, self.lb98, self.lb99, self.lb100]
        points = 0
        count_enemys = random.randint(5, 20)
        player = "images/player.jpg"
        pole = "images/field.png"
        enemy = "images/enemy.png"
        map_ = [pole] * 100
        player_coord = random.randint(0, 99)
        map_[player_coord] = player
        for i in range(1, count_enemys + 1):
            self.add_en()
        self.print_()
        t = threading.Thread(target=self.start, args=())
        t.start()

    def add_en(self):
        global player, enemy, map_
        coord = random.randint(0 , 99)
        if map_[coord] != player and map_[coord] != enemy:
            map_[coord] = enemy
        else:
            self.add_en()
    def print_(self):
        global points, check, map_
        os.system("cls")
        for i in range(100):
            check[i].setPixmap(QPixmap(map_[i]))
        self.label.setText(f"Поймано врагов: {points}")
        time.sleep(0.1)

    def check(self):
        global player_coord, points, flag
        if map_[player_coord] == enemy:
            points += 1


    def plus(self, count):
        global player_coord, pole, map_
        map_[player_coord] = pole
        if count == 10 and player_coord + 10 > 99:
            player_coord = player_coord%10
        elif count == 1 and player_coord == 99:
            player_coord = 0
        else:
            player_coord += count
        self.check()
        map_[player_coord] = player

    def minus(self, count):
        global player_coord, pole, map_
        map_[player_coord] = pole
        if count == 10 and player_coord - 10 < 0:
            player_coord = 90 + player_coord
        elif count == 1 and player_coord == 0:
            player_coord = 99
        else:
            player_coord -= count
        self.check()
        map_[player_coord] = player
    def start(self):
        global count_enemys, points
        while count_enemys != points:
            if keyboard.is_pressed("esc"):
                exit()
            elif keyboard.is_pressed('w'):
                self.minus(10)
                self.print_()
            elif keyboard.is_pressed('a'):
                self.minus(1)
                self.print_()
            elif keyboard.is_pressed('s'):
                self.plus(10)
                self.print_()
            elif keyboard.is_pressed('d'):
                self.plus(1)
                self.print_()
        self.label.setText("Вы выйграли!!")

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)
if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())