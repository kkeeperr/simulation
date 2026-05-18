from app.coordinates import Coordinates


class Entity:
    icon: str = '' 
    coordinates: Coordinates
    
    def __init__(self, coordinates):
        self.coordinates = coordinates
