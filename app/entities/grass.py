from app.entities.entity import Entity


class Grass(Entity):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.icon = '🌿'