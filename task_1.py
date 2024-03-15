import math

class Circle:
    def __init__(self, coords: tuple, radius: float):
        self.coords: tuple[float] = coords
        self.radius: float = radius
        
    def get_circumference(self) -> float:
        return 2 * math.pi * self.radius
    
    def __repr__(self) -> str:
        return f"Circle({self.coords}, {self.radius})"
        
    def __eq__(self, other: object) -> bool:
        return self.radius == other.radius
    
    def __lt__(self, other: object) -> bool:
        return self.get_circumference() < other.get_circumference()
    
    def __le__(self, other: object) -> bool:
        return self.get_circumference() <= other.get_circumference()
    
    def __gt__(self, other: object) -> bool:
        return self.get_circumference() > other.get_circumference()
    
    def __ge__(self, other: object) -> bool:
        return self.get_circumference() >= other.get_circumference()
    
    def __add__(self, other: object):
        return Circle(self.coords, self.radius + other.radius)
    
    def __iadd__(self, other: object):
        self.radius += other.radius
        return self
    
    def __sub__(self, other: object):
        return Circle(self.coords, self.radius - other.radius)
    
    def __isub__(self, other: object):
        self.radius -= other.radius
        return self
