from ..kri_cipher import Template,Encrypt
from .schemas.Input import Input
from .schemas.Keys import KeysContainer
"""
@author: Israel Alejandro Herrera Araiza
@author: IISP

!implementacion de protocolo DiffHellman

"""
class DiffHellman(Template,Encrypt):
    def generateKey(self):

        return super().generateKey()
    def input(self):
        self.enrtyPoint.p = int(self._input("p","ingrese un numero primo: "))
        # se enviara por la red
        roots = self.generatePrimitiveRoots(self.enrtyPoint.p)
        # se selecciona un numero a que se comparte en la red

        self.output(roots)

        self.enrtyPoint.a = int(self._input("a","selecciona un numero de la matriz de valores: "))
        
        self.KEYS_CONTAINER.cp = self.validateKey(int(self._input("cp","coloca la clave privda propia: ")),self.enrtyPoint.p)
        self.KEYS_CONTAINER.cu = self.generatePublicKey(self.enrtyPoint.a,self.KEYS_CONTAINER.cp,self.enrtyPoint.p)
        self.output(f"clave publica generada: {self.KEYS_CONTAINER.cu} ")
        self.KEYS_CONTAINER.yb  = int(self._input("yb","clave publica del receptor: "))
       
    def validateKey(self,cp,p):
        if not(cp < p):
            raise ValueError("la clave privada debe ser menor al numero primo seleccionado")
        return cp
    @staticmethod
    def generateKeySession(yb,cp,p):
        return (yb**cp)%p
    @staticmethod
    def generatePublicKey(a,cp,p):
        return (a**cp)%p
    @staticmethod
    def generatePrimitiveRoots(p) -> list[int]:
        # regla a < p  donde a es la raiz primitiva
        # eq en ejemplo: [x for x in range(3,p) if DiffHellman.is_generator(x,p)]
        return [x for x in range(p) if DiffHellman.is_generator(x,p)]
    @staticmethod
    def is_generator(g, p):
        """
        EL CALCULO DE LOS GENERADORES DEL NUMERO
        por 
        Israel Alejandro Herrera Araiza
        """
        generated = []
        for i in range(1, p):
            e = pow(g, i, p)
            if e in generated:
                return False
            else:
                generated.append(e)

        if len(generated) == p - 1:
            return True
    def output(self, *args):
        print(args)
        for idx,x in enumerate(args):
            self._output(str(idx),args)
    def encrypt(self, m):
        self.KEYS_CONTAINER.channelKey = self.generateKeySession(self.KEYS_CONTAINER.yb,self.KEYS_CONTAINER.cp,self.enrtyPoint.p)
        self.output(self.KEYS_CONTAINER.channelKey)
        return self.KEYS_CONTAINER.channelKey
    def configurations(self,input,output):
        self.enrtyPoint = Input()
        self.KEYS_CONTAINER =  KeysContainer()
        self._input = lambda nme,o: input.print(**{nme:o}).value[nme]
        self._output = lambda nme,o: output.output(**{nme:o})
    