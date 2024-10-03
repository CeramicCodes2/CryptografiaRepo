from abc import ABC,abstractmethod
from dataclasses import asdict
class AbastractField(ABC):
    def export(self):
        return asdict(self)
    @abstractmethod
    def isFilled(self) -> bool:
        ...
    @abstractmethod
    def reset(self):
        ...
    @abstractmethod
    def include(self,**kwargs):
        ...
