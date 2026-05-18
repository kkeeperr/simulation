from app.entities.creature import Creature
from app.entities.hibervivor import Hibervivor


class Predator(Creature):
    MAX_HEALTH = 10

    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.icon = "🐺"
        self.health = self.MAX_HEALTH
        self.food = Hibervivor

    def eat(self):
        self.health = self.MAX_HEALTH
        self.hungry = 0
