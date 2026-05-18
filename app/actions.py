from collections import deque

from app.coordinates import Coordinates
from app.entities.creature import Creature
from app.entities.grass import Grass
from app.entities.hibervivor import Hibervivor
from app.entities.predator import Predator
from app.map import Map


class Actions:
    map: Map

    def __init__(self, map: Map):
        self.map = map

    def init_actions(self):
        self.map.generation()

    def turn_actions(self):
        entities = list(self.map.map.values())
        for entity in entities:

            if isinstance(entity, Creature):

                path, food_coord = self.find_path(entity)
                old_coord = entity.coordinates
                if not path:
                    entity.starve()
                    if not entity.is_alive():
                        self.map.map.pop(entity.coordinates)
                    continue
                new_coord = entity.make_move(path)
                self.map.map.pop(old_coord)
                if isinstance(self.map.map.get(new_coord), entity.food):
                    self.map.map.pop(new_coord)
                    entity.eat()
                else:
                    entity.starve()
                    if not entity.is_alive():
                        continue

                self.map.map[new_coord] = entity

        grass_count = self.counter_population(entities, Grass)
        self.update_population(grass_count, Grass)
        hibervivor_count = self.counter_population(entities, Hibervivor)
        self.update_population(hibervivor_count, Hibervivor)
        predator_count = self.counter_population(entities, Predator)
        self.update_population(predator_count, Predator)

    def counter_population(self, entities, entity_type):
        counter = 0
        for entity in entities:
            if isinstance(entity, entity_type):
                counter += 1
        return counter

    def update_population(self, curr_count, entity_type):
        MAX_COUNT = {
            Grass: self.map.GRASS_MAX_COUNT,
            Hibervivor: self.map.HIRBEVIVOR_MAX_COUNT,
            Predator: self.map.PREDATOR_MAX_COUNT,
        }
        if curr_count * 2 <= MAX_COUNT.get(entity_type):
            self.map.factory.create_entities(
                self.map.map,
                curr_count,
                self.map.height,
                self.map.width,
                entity=entity_type,
            )

    def find_path(self, entity):
        moves = deque()
        visited = set()
        came_from = {}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        start = entity.coordinates
        moves.append(start)
        visited.add(start)

        food_coord = None
        while moves:
            curr = moves.popleft()
            for dx, dy in directions:
                new_x = curr.x + dx
                new_y = curr.y + dy
                if 0 <= new_x < self.map.width and 0 <= new_y < self.map.height:
                    new_coordinates = Coordinates(new_x, new_y)
                    if (
                        new_coordinates not in self.map.map
                        and new_coordinates not in visited
                    ):
                        moves.append(new_coordinates)
                        visited.add(new_coordinates)
                        came_from[new_coordinates] = Coordinates(curr.x, curr.y)

                    elif isinstance(self.map.map.get(new_coordinates), entity.food):
                        food_coord = new_coordinates
                        came_from[new_coordinates] = Coordinates(curr.x, curr.y)
                        break

            if food_coord:
                break

        if food_coord is None:
            return [], None

        curr = food_coord
        path = []
        while curr != start:
            path.append(curr)
            curr = came_from[curr]

        path.reverse()
        return path, food_coord
