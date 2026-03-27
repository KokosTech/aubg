# abstract classes

from abc import ABC, abstractmethod
from copy import deepcopy

class BaseAddress(ABC):
    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def display(self):
        pass


class Address(BaseAddress):
    def __init__(self, details: dict):
        self.details = details

    def __str__(self):
        msg = super().__str__()
        for item in self._details:
            msg += f"\n{item}: {self._details[item]}"
        return msg

    def display(self):
        print(self)

    @property
    def details(self) -> dict:
        return self._details

    @details.setter
    def details(self, details: dict):
        self._details = deepcopy(details)

    def __getitem__(self, key):
        return self._details[key]

    def __getattr__(self, key):
        return self._details[key]
    
    def __eq__(self, other):
        if not isinstance(other, Address):
            return NotImplemented
        
        same = True 
        
        for item in self._details:
            if item not in other._details:
                continue
            if self._details[item] != other._details[item]:
                same = False
                break
            
        return same

class HomeAddress(Address):
    def __init__(self, details: dict):
        super().__init__(details)
        

class WorkAddress(Address):
    def __init__(self, details: dict):
        super().__init__(details)

addr = Address({'city': 'Sofia', 'country': 'Bulgaria', 'blvd': 'Vitosha'})
print(addr['country'])  # __getitem__
print(addr.country)  # __getattr__

addr2 = HomeAddress({'city': 'Sofia', 'country': 'Bulgaria', 'blvd': 'Vitosha'})
print(addr2)