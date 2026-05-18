import random

from app.coordinates import Coordinates


class Factory:

    @staticmethod
    def create_entities(map: dict, entity_count, height, width, entity):
        curr_count = 0

        if entity_count == 0:
            return map

        if len(map) >= height * width:
            return map

        free_cells = height * width - len(map)
        entity_count = min(entity_count, free_cells)

        while True:
            rand_x = random.randint(0, width - 1)
            rand_y = random.randint(0, height - 1)
            coordinates = Coordinates(rand_x, rand_y)

            if coordinates not in map.keys():
                map[coordinates] = entity(coordinates)
                curr_count += 1

                if curr_count == entity_count:
                    return map
