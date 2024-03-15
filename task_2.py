class Complex:
    def __init__(self, r: float, i: float):
        self.r: float = r
        self.i: float = i
        
    def get_real(self) -> float:
        return self.r
    
    def get_imaginary(self) -> float:
        return self.i
    
    def __repr__(self) -> str:
        if self.i > 0:
            return f"{self.r} + {self.i}i"
        elif self.i < 0:
            return f"{self.r} - {-self.i}i"
        else:
            return f"{self.r}"
        
    def __add__(self, other: object):
        return Complex(self.r + other.r, self.i + other.i)
    
    def __iadd__(self, other: object):
        self.r += other.r
        self.i += other.i
        return self
    
    def __sub__(self, other: object):
        return Complex(self.r - other.r, self.i - other.i)
    
    def __isub__(self, other: object):
        self.r -= other.r
        self.i -= other.i
        return self
    
    def __mul__(self, other: object):
        new_r = self.r * other.r - self.i * other.i
        new_i = self.r * other.i + other.r * self.i
        return Complex(new_r, new_i)
    
    def __truediv__(self, other: object):
        new_r = (self.r * other.r + self.i * other.i) / (other.r ** 2 + other.i ** 2)
        new_i = (other.r * self.i - self.r * other.i) / (other.r ** 2 + other.i ** 2)
        return Complex(new_r, new_i)
