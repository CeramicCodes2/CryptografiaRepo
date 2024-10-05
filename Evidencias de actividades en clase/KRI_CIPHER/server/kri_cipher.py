# USAREMOS TEMPLATE METHOD PATTERN PARA REALIZAR EL PROGRAMA MENU
from abc import ABC,abstractmethod
from typing import TypeVar,Generic
from string import ascii_letters
class Encrypt(ABC):
    @abstractmethod
    def encrypt(self,m):
        ...
class Decrypt(ABC):
    @abstractmethod
    def decrypt(self,m):
        ...
class Template(ABC):
    def __init__(self,input,output) -> None:
        self.main(input,output)
    def encode(self,message:str):
        return [ord(x) for x in message]

    def main(self,input,output):
        # template method
        self.configurations(input,output)
        self.input()
        self.generateKey()
        e = self.encrypt() 
        self.output(f"[*] mensaje: {27}")
        self.output(f"[*] criptograma: {e}")
        if isinstance(self,Decrypt):
            self.output(f"[*] texto descifrado: {self.decrypt(e)}")
    @abstractmethod
    def generateKey(self):
        ...
    @abstractmethod
    def input(self):

        ...
    @abstractmethod
    def output(self,*args):
        ...

    @abstractmethod
    def configurations(self,input,output):
        # INPUT Y OUTPUT SON DEPENDENCIAS QUE SERAN UN OBSERVER 
        # metodo para configuracion de los cifrados 
        # por ejemplo en rsa es posible establecer numeros maximos para la generacion de la clave publica
        ...
  
# OBSERVER FOR ABSTRACT THE COMMUNICATION PROCESS
class Observer(ABC):
    @abstractmethod
    def update(self,subject):
        # send a signal of a concrete event to all the suscriptors
        ...

class Subject(ABC):
    @property
    @abstractmethod
    def state(self):
        ...
    @abstractmethod
    def suscribe(self,observer:Observer):
        ...
    @abstractmethod
    def unsuscribe(self,observer:Observer):
        ...
    @abstractmethod
    def notify(self):
        ...
T = TypeVar("T")
class State(Generic[T]):
    def __init__(self) -> None:
        self._value = None
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,arg):
        self._value= arg
    def isPresent(self):
        if self._value:
            return True 
        return False
 
class EventObservableHandler(Subject):
    def __init__(self,state) -> None:
        self._suscribers:list[Observer] = []
        self._state:State = state
    @property
    def state(self) -> State:
        return self._state
    @state.setter
    def state(self,state):
        self._state.value = state
    @state.deleter
    def state(self):
        self._state.value = None

    def suscribe(self, observer: Observer):
        self._suscribers.append(observer)
        return super().suscribe(observer)
    def unsuscribe(self, observer: Observer):
        self._suscribers.remove(observer)
        return super().unsuscribe(observer)
    def notify(self):

        [x.update(self) for x in self._suscribers]
        return super().notify()

        

class Input:
    def __init__(self,handler:EventObservableHandler, state=State[dict[str,str]]()) -> None:
        self.handler = handler
    def print(self,**kwargs):
        # depende de la implementacion como manejar estos argumentos de estado
        self.handler.state = kwargs
        # seteamos valores 
        self.handler.notify()
        return self.handler.state

class Output:
    def __init__(self,handler:EventObservableHandler,state=State[dict[str,str]]()) -> None:
        self.handler = handler
    def output(self,**kwargs):
        # depende de la implementacion como manejar estos argumentos de estado
        self.handler.state = kwargs
        # seteamos valores 
        self.handler.notify()