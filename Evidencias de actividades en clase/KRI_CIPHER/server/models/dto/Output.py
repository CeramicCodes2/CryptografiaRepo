from .Abstract import AbastractField
from dataclasses import dataclass,asdict,field
@dataclass
class OutputDto(AbastractField):
    messages:list[str] = field(default_factory=lambda: [])
    def export(self):
        return asdict(self)
    def isFilled(self) -> bool:
        return True

    def reset(self):
        
        self.messages.clear()
    def include(self,**kwargs):
        if kwargs:
            self.messages.extend([{k:x} for k,x in kwargs.items()])
