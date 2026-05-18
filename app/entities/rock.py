from app.entities.entity import Entity


class Rock(Entity):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.icon = '🗿'