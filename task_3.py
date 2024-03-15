class Airplane:
    def __init__(self, type: str, capacity: int, pax: int):
        self.type: str = type
        self.capacity: int = capacity
        if 0 <= pax <= self.capacity:
            self.pax: int = pax
        elif pax > self.capacity:
            self.pax: int = capacity
        else:
            self.pax: int = 0
        
    def __str__(self) -> str:
        return f"{self.type}\t{self.capacity}\t{self.pax}"
    
    def __eq__(self, other: object) -> bool:
        return self.type.upper() == other.type.upper()
    
    # Operations + and - do not have sense for aircraft
    def __iadd__(self, other: object):
        self.pax += other.pax
        return self
    
    def __isub__(self, other: object):
        self.pax -= other.pax
        return self
    
    def __lt__(self, other: object) -> bool:
        return self.capacity < other.capacity
    
    def __le__(self, other: object) -> bool:
        return self.capacity <= other.capacity
    
    def __gt__(self, other: object) -> bool:
        return self.capacity > other.capacity
    
    def __ge__(self, other: object) -> bool:
        return self.capacity >= other.capacity