from os import system
from random import randrange

class Nodo:
    def __init__(self, previo=None, dato=None, siguiente=None):
        self.previo = previo
        self.dato = dato
        self.siguiente = siguiente

    def __str__(self):
        cadena =''
        if self.previo != None:
            cadena += '<- '

        cadena += '| ' + str(self.dato) + ' |'

        if self.siguiente != None:
            cadena += ' ->'
        
        return cadena
    
class LDE:
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

    def insertaAlInicio(self, dato):
        if self.estaVacia():
            self.primero = Nodo(None, dato, None)
            self.ultimo = self.primero
        else:
            self.primero.previo = Nodo(None, dato, self.primero)
            self.primero = self.primero.previo

    def insertaAlFinal(self, dato):
        if self.estaVacia():
            self.ultimo = Nodo(None, dato, None)
            self.primero = self.ultimo
        else:
            self.ultimo.siguiente = Nodo(self.ultimo, dato, None)
            self.ultimo = self.ultimo.siguiente
        
    def muestra(self):
        aux = self.primero
        while aux != None:
            print(aux, end='')
            aux = aux.siguiente

    def muestraInvretida(self):
        aux = self.ultimo
        while aux != None:
            if aux.siguiente != None:
                print('<- ', end='')
            print(f'| {aux.dato} |', end='')
            if aux.previo != None:
                print(' ->', end='')
            aux = aux.previo

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
            self.primero.previo = None
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
            aux = self.ultimo
            x = self.ultimo.dato
            self.ultimo = self.ultimo.previo
            self.ultimo.siguiente = None
            del aux
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
                aux1 = aux2.siguiente
                aux1.previo = aux2.previo
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

            aux1.siguiente = Nodo(aux1, dato, aux2)
            aux2.previo = aux1.siguiente


if __name__ == '__main__':
    system('cls')
    L = LDE()
    n = randrange(11)
    for i in range(n):
        x = randrange(101)
        print(f'Se inserta {x}')
        L.inserta(x)

    print('\n\nL  -> ', end='')
    L.muestra()
    print()
    print('LI -> ', end='')
    L.muestraInvretida()
    print('\n\n')

    if not L.estaVacia():
        print(f'Se elimina {L.eliminaAlInicio()}')
        L.muestra()
        print('\n\n')

    if not L.estaVacia():
        print(f'Se elimina {L.eliminaAlFinal()}')
        L.muestra()
        print()
        print('\n\n')

    x = int(input('A quién eliminas? '))
    if L.elimina(x):
        print(f'SE eliminó {x} =)')
    else:
        print(f'NO se eliminó {x} =(')
    L.muestra()
    print('\n\n')
