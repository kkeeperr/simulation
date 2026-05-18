import os
import threading
import time

import readchar

from app.map import Map
from app.actions import Actions


class Simulation:
    height: int
    width: int
    map: Map
    actions: Actions
    moves_count: int
    paused: bool

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = Map(height, width)
        self.actions = Actions(self.map)
        self.moves_count = 0
        self.paused = False

    def start_simulation(self):

        self.actions.init_actions()
        thread = threading.Thread(target=self.pause_simulation, daemon=True)
        thread.start()

        while True:
            self.moves_count += 1
            self.next_turn()

    def next_turn(self):
        while self.paused:
            time.sleep(0.1)

        os.system("cls")
        print("Нажмите SPACE для паузы!")
        self.map.render()
        print(f"Текущий ход: {self.moves_count}")
        time.sleep(1)
        self.actions.turn_actions()

    def pause_simulation(self):
        while True:
            key = readchar.readkey()
            if key == " ":
                self.paused = not self.paused
