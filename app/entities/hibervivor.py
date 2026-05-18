from app.entities.creature import Creature
from app.entities.grass import Grass


class Hibervivor(Creature):
    MAX_HEALTH = 5

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.health = self.MAX_HEALTH
        self.icon = "🐇"
        self.food = Grass

    def eat(self):
        self.health = self.MAX_HEALTH
        self.hungry = 0
