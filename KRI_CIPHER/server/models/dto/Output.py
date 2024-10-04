from .Abstract import AbastractField
from dataclasses import dataclass,asdict
@dataclass
class OutputDto(AbastractField):
    messages:list[str]
    def export(self):
        return asdict(self)
    def isFilled(self) -> bool:
        return True

    def reset(self):
        self.messages = []
    def include(self,**kwargs):
        if kwargs:
            self.messages.extend([{k:x} for k,x in kwargs.items()])
