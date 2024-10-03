from dataclasses import dataclass,asdict
from json import dumps
@dataclass
class KeysContainer:
    cp:int = 0# clave privada
    # debe ser menor al numero primo
    cu:int = 0
    yb:int = 0# clave publica del contrincante
    channelKey:int = 0
    def __str__(self):
        return dumps(asdict)
    def export(self):
        return asdict(self)