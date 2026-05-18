from abc import ABC, abstractmethod
from collections import deque

from app.coordinates import Coordinates
from app.entities.entity import Entity


class Creature(Entity, ABC):

    health: int
    speed: int
    hungry: int
    food: Entity

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.speed = 1
        self.hungry = 0
        self.food = None

    def make_move(self, path: list):
        for step in range(self.speed):
            if step < len(path):
                self.coordinates = path[step]

        return self.coordinates

    def starve(self):
        self.hungry += 1
        if self.hungry > 5:
            self.health -= 1

    def is_alive(self):
        if self.health <= 0:
            return False
        return True

    @abstractmethod
    def eat(self):
        pass
