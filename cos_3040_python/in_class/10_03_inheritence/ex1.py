import math

class Shape():
    def __init__(self):
        pass
    
    @property
    def get_area(self):
        pass
    
    @property
    def get_perimeter(self):
        pass
    
    
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
    
    @a.setter
    def a(self, a: float):
        if a <= 0:
            raise ValueError("Side lengths must be positive.")
        self._a = a
    
    @b.setter
    def b(self, b: float):
        if b <= 0:
            raise ValueError("Side lengths must be positive.")
        self._b = b
        
    @c.setter
    def c(self, c: float):
        if c <= 0:
            raise ValueError("Side lengths must be positive.")
        self._c = c
        
    @property
    def a(self):
        return self._a
    
    @property
    def b(self):   
        return self._b
    
    @property
    def c(self):
        return self._c
    
    @property
    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    @property
    def get_perimeter(self):
        return self.a + self.b + self.c
    
class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius
    
    @radius.setter
    def radius(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @property
    def get_area(self):
        return math.pi * self._radius ** 2

    @property
    def get_perimeter(self):
        return 2 * math.pi * self._radius
