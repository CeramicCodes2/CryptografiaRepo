from ..kri_cipher import Template,Encrypt,Decrypt
from .schemas.input import Input
from .schemas.keys import KeysContainer
from secrets import choice
"""
@author: IISP
!DISCLAMER: ESTA ES UNA IMPLEMENTACION DE LIBRO, SE DESACONSEJA SU USO PARA PRODUCCION

"""
class RSA(Template,Encrypt,Decrypt):
    def encrypt(self,m) -> int:
        return pow(m,self.PBPK_CONTAINER.e,self.PBPK_CONTAINER.n)# simplificacion de :(m**self.PBPK_CONTAINER.e)%self.PBPK_CONTAINER.n

    def decrypt(self,m) -> int:
        return pow(m,self.PBPK_CONTAINER.d,self.PBPK_CONTAINER.n)# (m**self.PBPK_CONTAINER.d)%self.PBPK_CONTAINER.n

    @staticmethod
    def primeChecker(number:int):
        # Funcion adaptada de Azad Saiful
        if(number<2): return False
        # e siempre debe ser mayor que 2
        c = 2
        while (c<number/2):
            if(not(number%c)): return False
            c+= 1
        return True
    @staticmethod
    def eulerTotientFunction(p,q):
        # calculo de funcion totiente de euler
        return (p-1) * (q-1)
    @staticmethod
    def findMaxCoprimeNumber(phi,e=2,auto=False):
        # busqueda de un numero coprimo de phi (es decir E)
        # e debe ser > 1 pero menor que phi
        # retornara el coprimo mas alto
        return choice([ x for x in range(2,phi) if RSA.egcd(phi,x)[0]==1])#max([ x for x in range(2,phi) if RSA.egcd(phi,x)[0]==1 and x.is_integer()])
    @staticmethod
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = RSA.egcd(b % a, a)
            return (g, y - (b // a) * x, x)
    @staticmethod
    def checkCoprime(a:int,b:int) -> bool:
        # podemos implementrar euclides extendido 
        l = 0
        if(a>b):
            l = b
        c = 2# como se dijo e siempre tiene que ser mayora 1
        # l puede ser phi(n)
        while (c<l):
            if(not(a%c) and not(b%c)):
                # si no es modular de ambos entonces no es coprimo
                # recuerda un numero es cooprimo cuando con otro numero 
                # denomiado d su modular da 0 osea que es congruente
                c += 1
                # no hay nada asi que incrementamos
        return True
    def findCoprime(self,phi):
        if self.entryPoint.auto:
            return self.findMaxCoprimeNumber(phi,self.entryPoint.e,auto = True)
        return self.findMaxCoprimeNumber(phi,self.entryPoint.e)



        
    def findComprimeD(self,phi,e) ->int:
        d = lambda k,phi,e: (1+(k*phi))/e
        
        pd:int = 2
        for x in range(1,phi):
            pd = d(x,phi,e)
            print(pd)
            if pd.is_integer():
                print(pd)
                return int(pd)
            continue
        return self.findComprimeD(phi,e)# si no se encontro uno
    def generateKey(self):
        # generacion de clave
        p,q = self.entryPoint.p,self.entryPoint.q
        print(p,q)
        
        if not(self.primeChecker(p) and self.primeChecker(q)): raise ValueError("DATOS INVALIDOS ! P Y Q DEBEN SER NUMERO PRIMOS !\n")
        N = p*q
        phi = self.eulerTotientFunction(p,q)
        #e = self.entryPoint.get("e",2)
        e = self.findCoprime(phi)
        self.entryPoint.e = e

        # coprimo de e ahora lo buscamos
        # para poder realizar el descifrado de los datos
        d = self.findComprimeD(phi,e)
        print(d)
        print("cc",e,d)
        self.output(d)
        if not((e*d)%phi == 1):
            raise ValueError("Error de calculo los numeros seleccionados no generaron una congruencia")
        self.PBPK_CONTAINER = KeysContainer(e=e,d=d,n=N)
        self.output(f"[*] Clave publica generada: {e} \n [*] Clave privada generada: {d}")

    def configurations(self,input,output):
        self.MAX_VAREABLE_D = 2048

        self.entryPoint = Input()
        self._input = lambda nme,o: input.print(**{nme:o}).value[nme]
        self._output = lambda nme,o: output.output(**{nme:o})

        return super().generateKey()
    def input(self):
        
        #self.entryPoint.message = self._input("ingrese su mensaje:")
        self.entryPoint.p = int(self._input("p","ingrese un numero p:"))
        self.entryPoint.q = int(self._input("q","ingrese un numero q:"))
        i = self._input("auto","usar auto generacion de e ? (y/n): ").upper()
        if not(i.find("Y") == 0):
            e=int(self._input("e","Ingrese un numero para e:"))
            self.entryPoint.auto["e"] = e
        return self.entryPoint.export()


    def output(self, *args):
        print(args)
        for idx,x in enumerate(args):
            self._output(str(idx),args)

"""


import math
from itertools import combinations
def frequency_distance_repeat(tuples):
    frequency_len = {} #Dict con {mcd:frecuencia}
    distancias = []
    for i in range(len(tuples)): #Iteramos la lista de tuplas
        distancias.append(tuples[i][1]) # añadimos el valor a la lista de distancias
    comb = combinations(distancias,2) # Obtenemos las combinaciones posibles de distancias 2 a 2
    for i in list(comb): # Para cada posible combinación
        gcd = math.gcd(i[0],i[1]) #obtenemos maximo comun divisor y la frecuencia de aparición
        if gcd not in frequency_len and gcd > 1: 
            frequency_len[gcd] = 1
        else:
            if gcd > 1:
                frequency_len[gcd] = frequency_len[gcd]+1
    return frequency_len


ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MSJ = "HOLA MUNDO DEL CRIPTOANALISIS PROBANDO EL CIFRADO CESAR"
# encode2way
encode = lambda MSJ: [ALPHABET.index(x) for x in MSJ]
# decode
decode = lambda vector: "".join([ALPHABET[x] for x in vector])

# encrypt
cesar = lambda TOKEN: [(x+3)%len(ALPHABET) for x in TOKEN]
c = cesar(encode(MSJ))
print(f"[*] CRIPTOGRAMA: {decode(c)}")
print(f"[*] INICIANDO ANALISIS DE COINCIDENCIAS")

def frequencyAnalysis(encodedText:list[int]) -> dict[int,int]:
    frequences = dict()
    for idx,e in enumerate(set(encodedText)):
        frequences[e] = encodedText.count(e)
    return frequences
def ic(freq_list,lon):
    return sum([abs(freq_list.get(letter,0)* 100 /len(text)-letter_freq_sp[letter]) for letter in alfabeto]) / len(alfabeto)
freq = letter_freq_sp={"A":11.72,"B":1.49,"C":3.87,"D":4.67,"E":13.72,"F":0.69,"G":1.00,"H":1.18,"I":5.28,"J":0.52,"K":0.11,"L":5.24,"M":3.08,"N":6.83,"Ñ":0.17,"O":8.44,"P":2.89,"Q":1.11,"R":6.41,"S":7.20,"T":4.60,"U":4.55,"V":1.05,"W":0.04,"X":0.14,"Y":1.09,"Z":0.47} 

freq = frequencyAnalysis(c)
ioc = ic(freq,len(c))
print(f"[*] CANTIDAD DE DESPLAZAMIENTO: {ioc} {freq}")



ev = [e for e,l in zip(range(0,phi),([1]*20)) if gcd(e,phi) == 1]
d = [((1+(k*phi))/e) for k in range(0,phi-1)]


"""