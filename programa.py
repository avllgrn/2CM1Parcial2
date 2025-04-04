from os import system
from random import randrange

class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def __str__(self):
        cadena = '| ' + str(self.dato) + ' |'

        if self.siguiente != None:
            cadena += ' -> '
        
        return cadena
    
class LSE:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def __del__(self):
        self.liberaMemoria()
    
    def estaVacia(self):
        return self.primero ==  None and self.ultimo == None
    
    def liberaMemoria(self):
        while not self.estaVacia():
            x = self.eliminaAlInicio()
            #print(f'Se elimina {x}')

    def generaListaOrdenada(self, n):
        self.liberaMemoria()
        for i in range(n):
            x = randrange(101)
            # print(f'Se inserta {x}')
            self.inserta(x)

    def generaListaDesordenada(self, n):
        self.liberaMemoria()
        for i in range(n):
            x = randrange(101)
            # print(f'Se inserta {x}')
            self.insertaAlFinal(x)

    def insertaAlInicio(self, dato):
        if self.estaVacia():
            self.primero = Nodo(dato, None)
            self.ultimo = self.primero
        else:
            self.primero = Nodo(dato, self.primero)

    def insertaAlFinal(self, dato):
        if self.estaVacia():
            self.ultimo = Nodo(dato, None)
            self.primero = self.ultimo
        else:
            self.ultimo.siguiente = Nodo(dato, None)
            self.ultimo = self.ultimo.siguiente
        
    def muestra(self):
        aux = self.primero
        while aux != None:
            print(aux, end='')
            aux = aux.siguiente

    def busca(self, dato):
        aux = self.primero
        while aux != None:
            if aux.dato == dato:
                return True
            aux = aux.siguiente

        return False

    def eliminaAlInicio(self):
        if self.estaVacia():
            return None
        elif self.primero==self.ultimo:
            x = self.primero.dato
            del self.primero
            self.primero=None
            self.ultimo=None
        else:
            aux = self.primero
            x = aux.dato
            self.primero = self.primero.siguiente
            del aux
        return x

    def eliminaAlFinal(self):
        if self.estaVacia():
            return None
        elif self.primero==self.ultimo:
            x = self.ultimo.dato
            del self.ultimo
            self.ultimo=None
            self.primero=None
        else:
            aux = self.primero
            x = self.ultimo.dato
            
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente

            del self.ultimo
            self.ultimo = aux
            self.ultimo.siguiente = None
        return x

    def elimina(self, dato):
        if self.estaVacia():
            return False
        elif dato == self.primero.dato:
            self.eliminaAlInicio()
            return True
        elif dato == self.ultimo.dato:
            self.eliminaAlFinal()
            return True
        else:
            aux1 = self.primero
            aux2 = self.primero.siguiente
            while aux2 != None and dato != aux2.dato:
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente
            if aux2 == None:
                return False
            else:
                aux1.siguiente = aux2.siguiente
                del aux2
                return True
            
    def inserta(self, dato):
        if self.estaVacia() or dato <= self.primero.dato:
            self.insertaAlInicio(dato)

        elif dato >= self.ultimo.dato:
            self.insertaAlFinal(dato)

        else:
            aux1 = self.primero
            aux2 = self.primero.siguiente

            while dato > aux2.dato:
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente

            aux1.siguiente = Nodo(dato, aux2)

    def concatena(self, OtraLista):
        L3 = LSE()

        aux = self.primero
        while aux!=None:
            L3.insertaAlFinal(aux.dato)
            aux=aux.siguiente


        aux = OtraLista.primero
        while aux!=None:
            L3.insertaAlFinal(aux.dato)
            aux=aux.siguiente

        return L3

    def uneOrdenadamente(self, OtraLista):
        L3 = LSE()

        aux1 = self.primero
        aux2 = OtraLista.primero
        while aux1!=None and aux2!=None:
            if aux1.dato <= aux2.dato:
                L3.insertaAlFinal(aux1.dato)
                aux1=aux1.siguiente
            else:
                L3.insertaAlFinal(aux2.dato)
                aux2=aux2.siguiente

        while aux1!=None:
            L3.insertaAlFinal(aux1.dato)
            aux1=aux1.siguiente

        while aux2!=None:
            L3.insertaAlFinal(aux2.dato)
            aux2=aux2.siguiente
        return L3
    
    def muestraInvertida(self):
        if not self.estaVacia():
            auxP = self.primero
            auxU = self.ultimo
            while auxP!=auxU:
                print(f'| {auxU.dato} | <-', end=' ')

                while auxP.siguiente!=auxU:
                    auxP = auxP.siguiente
                
                auxU = auxP
                auxP = self.primero
                
            print(f'| {auxU.dato} |', end=' ')

    def copia(self, Destino):
        Destino.liberaMemoria()
        aux=self.primero
        while aux!=None:
            Destino.insertaAlFinal(aux.dato)
            aux=aux.siguiente
        

def generaInvertida(Origen, Destino):
    Destino.liberaMemoria()
    aux=Origen.primero
    while aux!=None:
        Destino.insertaAlInicio(aux.dato)
        aux=aux.siguiente
    
if __name__ == '__main__':
    system('cls')

    L = LSE()
    I = LSE()

    n = randrange(11)
    L.generaListaOrdenada(n)

    generaInvertida(L, I)

    L.muestra()
    print()
    I.muestra()
    print()
