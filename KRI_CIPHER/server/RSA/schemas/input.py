from dataclasses import dataclass,asdict,field
from typing import Dict
@dataclass
class Input:
    p:int = 0
    q:int = 0
    e:int = 2
    #message:str = ""
    auto:Dict[str,bool|int] = field(default_factory=lambda: dict([("response",0),("e",0)]))
    
    def export(self) -> dict:
        dct = asdict(self)
        dct["e"] = dct["auto"]["e"]
        del dct["auto"]["e"]
        return dct