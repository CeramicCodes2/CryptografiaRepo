from dataclasses import dataclass,asdict
@dataclass
class KeysContainer:
    d:int
    e:int
    n:int
    def export(self):
        return asdict(self)
