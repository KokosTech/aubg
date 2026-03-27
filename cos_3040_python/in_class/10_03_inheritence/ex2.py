class Animal():
    def __init__(self, kind: str, is_mammal: bool, num_legs: int):
        self._kind = kind
        self._is_mammal = is_mammal
        self._num_legs = num_legs

    def hello(self):
        print(self._kind)
    
    @property
    def is_mammal(self):
        return self._is_mammal
        
    @property
    def num_legs(self):
        return self._num_legs
    
    
class Dog(Animal):
    def __init__(self):
        super().__init__(kind="Dog", is_mammal=True, num_legs=4)


class Cat(Animal):
    def __init__(self):
        super().__init__(kind="Cat", is_mammal=True, num_legs=4)


class Bird(Animal):
    def __init__(self):
        super().__init__(kind="Bird", is_mammal=False, num_legs=4)


class Pig(Animal):
    def __init__(self):
        super().__init__(kind="Pig", is_mammal=True, num_legs=4)
