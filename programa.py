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

    def muestraInvertida(self):
        aux = self.ultimo
        while aux != None:
            if aux.siguiente != None:
                print('<- ', end='')
            print(f'| {aux.dato} |', end='')
            if aux.previo != None:
                print(' ->', end='')
            aux = aux.previo

    def busca(self, dato):
        if self.estaVacia():
            return False
        else:
            aux1 = self.primero
            aux2 = self.ultimo
            while aux1!=aux2 and aux1.siguiente!=aux2:
                print(f'¿{aux1.dato} = {dato} o {aux2.dato} = {dato}?')
                if aux1.dato == dato or aux2.dato == dato:
                    return True
                aux1 = aux1.siguiente
                aux2 = aux2.previo

            if aux1==aux2 and aux1.dato==dato:
                print(f'¿{aux1.dato} = {dato} o {aux2.dato} = {dato}?')
                return True
            elif aux1.siguiente==aux2 and aux1.dato==dato:
                print(f'¿{aux1.dato} = {dato} o {aux2.dato} = {dato}?')
                return True
            elif aux1.siguiente==aux2 and aux2.dato==dato:
                print(f'¿{aux1.dato} = {dato} o {aux2.dato} = {dato}?')
                return True
            else:
                print(f'¿{aux1.dato} = {dato} o {aux2.dato} = {dato}?')
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
        if self.estaVacia() or (self.primero==self.ultimo and dato!=self.primero.dato):
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
            aux3 = self.ultimo
            aux4 = self.ultimo.previo

            # mietras los auxiliares no se encuentren en medio ni uno al lado del otro, ni el dato lo encuentre aux2 ni el dato lo encuentre aux4, despláza los auxiliares
            while aux2!=aux4 and aux2.siguiente!=aux4 and aux2.previo!=aux4 and dato != aux2.dato and dato != aux4.dato:
                print(f'¿{dato} = {aux2.dato}? o ¿{dato} = {aux4.dato}?')
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente
                aux3 = aux3.previo
                aux4 = aux4.previo            

            if dato!=aux2.dato and dato!=aux4.dato:
                print(f'¿{dato} = {aux2.dato}? o ¿{dato} = {aux4.dato}?')
                return False
            elif dato==aux2.dato:
                print(f'¿{dato} = {aux2.dato}? o ¿{dato} = {aux4.dato}?')
                aux1.siguiente = aux2.siguiente
                aux1 = aux2.siguiente
                aux1.previo = aux2.previo
                del aux2
                return True
            else:
                print(f'¿{dato} = {aux2.dato}? o ¿{dato} = {aux4.dato}?')
                aux3.previo = aux4.previo
                aux3 = aux4.previo
                aux3.siguiente = aux4.siguiente
                del aux4
                return True
            
    def inserta(self, dato):
        if self.estaVacia() or dato <= self.primero.dato:
            self.insertaAlInicio(dato)
        elif dato >= self.ultimo.dato:
            self.insertaAlFinal(dato)
        else:
            aux1 = self.primero
            aux2 = self.primero.siguiente
            aux3 = self.ultimo
            aux4 = self.ultimo.previo

            while dato >= aux2.dato and dato<=aux4.dato:
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente
                aux3 = aux3.previo
                aux4 = aux4.previo

            if dato < aux2.dato:
                aux1.siguiente = Nodo(aux1, dato, aux2)
                aux2.previo = aux1.siguiente
            else:
                aux4.siguiente = Nodo(aux4, dato, aux3)
                aux3.previo = aux4.siguiente


if __name__ == '__main__':
    system('cls')
    L = LDE()

    n = randrange(15)
    for i in range(n):
        x = randrange(11)
        print(f'Se inserta {x}')
        L.inserta(x)
        print('L  -> ', end='')
        L.muestra()
        print()
        print('LI -> ', end='')
        L.muestraInvertida()
        print('\n\n')

    input('Presiona una tecla para continuar...')
    system('cls')

    print('L  -> ', end='')
    L.muestra()
    print()
    print('LI -> ', end='')
    L.muestraInvertida()
    print('\n\n')

    n = randrange(15)
    for i in range(n):
        x = randrange(11)
        print(f'Se intenta buscar {x}')
        if L.busca(x):
            print(f'{x} FUE encontrado')
        else:
            print(f'{x} NO fue encontrado')

        print('L  -> ', end='')
        L.muestra()
        print()
        print('LI -> ', end='')
        L.muestraInvertida()
        print('\n\n')

    input('Presiona una tecla para continuar...')
    system('cls')

    print('L  -> ', end='')
    L.muestra()
    print()
    print('LI -> ', end='')
    L.muestraInvertida()
    print('\n\n')

    n = randrange(15)
    for i in range(n):
        x = randrange(11)
        print(f'Se intenta eliminar {x}')
        if L.elimina(x):
            print(f'{x} FUE eliminado')
        else:
            print(f'{x} NO fue eliminado')

        print('L  -> ', end='')
        L.muestra()
        print()
        print('LI -> ', end='')
        L.muestraInvertida()
        print('\n\n')
