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
        
    def estaVacia(self):
        return self.primero == None and self.ultimo == None

    def insertaAlInicio(self, dato):
        if self.estaVacia():
            self.primero = Nodo(dato, None)
            self.ultimo = self.primero
        else:
            self.primero = Nodo(dato, self.primero)

            

    def insertaAlFinal(self, dato):
        if self.estaVacia():
            self.ultimo = Nodo(dato, None)
            self.primero = self.primero
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
            if dato == aux.dato:
                return True
            aux = aux.siguiente        
        return False
    
    def eliminaAlInicio(self):
        aux =self.primero
        x = aux.dato
        self.primero = self.primero.siguiente
        del aux
        return x
    
    def eliminaAlFinal(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente

        x = self.ultimo.dato
        del self.ultimo
        aux.siguiente = None
        self.ultimo = aux
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
            while aux2!=None and dato != aux2.dato:
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente

            if aux2 == None:
                return False
            else:
                aux1.siguiente = aux2.siguiente
                return True           

    def inserta(self, dato):
        if self.estaVacia() or dato <= self.primero.dato:
            self.insertaAlInicio(dato)
        
        elif dato >= self.ultimo.dato:
            self.insertaAlFinal(dato)

        else:
            aux1 = self.primero
            aux2 = self.primero.siguiente

            while dato>aux2.dato:
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente

            aux1.siguiente = Nodo(dato, aux2)    

if __name__ == '__main__':
    system('cls')

    L = LSE()

    n = randrange(11)
    for i in range(n):
        L.inserta(randrange(101))
    L.muestra()
    print()

    cont = 0
    aux = L.primero
    while aux != None:
        cont = cont+1
        aux = aux.siguiente

    print(f'¿{n} == {cont}?')
