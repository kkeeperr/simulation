from app.coordinates import Coordinates
from app.entities.entity import Entity
from app.entities.grass import Grass
from app.entities.hibervivor import Hibervivor
from app.entities.predator import Predator
from app.entities.rock import Rock
from app.factory import Factory


class Map:
    map: dict[Coordinates, Entity]
    factory: Factory
    height: int
    width: int
    MAP_BG = "\033[43m"
    RESET_BG = "\033[0m"
    PREDATOR_MAX_COUNT: int
    HIRBEVIVOR_MAX_COUNT: int
    GRASS_MAX_COUNT: int
    ROCK_MAX_COUNT: int

    def __init__(self, height, width):
        self.map = {}
        self.factory = Factory()
        self.height = height
        self.width = width

        self.PREDATOR_MAX_COUNT = (height * width) // 20
        self.HIRBEVIVOR_MAX_COUNT = (height * width) // 10
        self.GRASS_MAX_COUNT = (height * width) // 5
        self.ROCK_MAX_COUNT = (height * width) // 10

    def generation(self):
        self.factory.create_entities(
            self.map, self.ROCK_MAX_COUNT, self.height, self.width, entity=Rock
        )
        self.factory.create_entities(
            self.map, self.GRASS_MAX_COUNT, self.height, self.width, entity=Grass
        )
        self.factory.create_entities(
            self.map,
            self.HIRBEVIVOR_MAX_COUNT,
            self.height,
            self.width,
            entity=Hibervivor,
        )
        self.factory.create_entities(
            self.map, self.PREDATOR_MAX_COUNT, self.height, self.width, entity=Predator
        )

    def render(self):
        for x in range(self.height):
            for y in range(self.width):
                coordinates = Coordinates(x, y)
                if coordinates in self.map:
                    entity = self.map.get(coordinates)
                    print(f"{self.MAP_BG}{entity.icon}", end="")
                else:
                    print(f"{self.MAP_BG}  ", end="")

            print(f' {self.RESET_BG}')
