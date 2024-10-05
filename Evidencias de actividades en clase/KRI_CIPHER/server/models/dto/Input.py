from dataclasses import dataclass,field
from typing import Dict
from .Abstract import AbastractField
@dataclass
class InputRsa(AbastractField):
    p:str = ""
    q:str = ""
    e:str = ""
    auto:Dict[str,bool|int] = field(default_factory=lambda: dict([("response",0),("e",0)]))
    def reset(self):
        self.p = ""
        self.q = ""
        self.e = "2"
        self.auto = {"response":"","e":2}
        return super().reset()
    def isFilled(self):
        if all([self.p,self.q,self.auto]) or all([self.p,self.q,self.e]):
            return True
        return False
    def include(self, **kwargs):
        for k,v in kwargs.items():
            for kk in vars(self).keys():
                if kk == k:
                    if k == "auto":
                        setattr(self,kk,v["response"])
                        setattr(self,"e",v["e"])
                        continue
                    setattr(self,kk,v)
                continue
@dataclass
class InputDiff(AbastractField):
    p:str = ""# numero primo
    a:str = ""# raices generadas
    cp:str = ""
    yb:str = ""
    def reset(self):
        self.p:int = 0
        self.a:int = 0
        return super().reset()
    def isFilled(self):
        if all([self.p]):
            return True
        return False
    def include(self, **kwargs):
        for k,v in kwargs.items():
            for kk in vars(self).keys():
                if kk == k:
                    setattr(self,kk,v)
                continue