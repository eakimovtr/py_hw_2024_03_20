class Flat:
    def __init__(self, area: float, price: float):
        self.area: float = area
        self.price: float = price
        
    def __eq__(self, other: object) -> bool:
        return self.area == other.area
    
    def __lt__(self, other: object) -> bool:
        return self.price < other.price
    
    def __le__(self, other: object) -> bool:
        return self.price <= other.price
    
    def __gt__(self, other: object) -> bool:
        return self.price > other.price
    
    def __ge__(self, other: object) -> bool:
        return self.price >= other.price
    
    
print(Flat(10, 100) > Flat(20, 50))