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
    
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def __del__(self):
        self.liberaMemoria()

    def push(self, d):
        if self.estaVacia():
            self.primero = self.ultimo = Nodo(d, self.primero)
        else:
            self.ultimo.siguiente = Nodo(d, self.primero)
            self.ultimo = self.ultimo.siguiente

    def pop(self):
        d = None
        if not self.estaVacia():
            d = self.primero.dato
            if self.primero == self.ultimo:
                del self.primero
                self.primero = self.ultimo = None
            else:
                aux = self.primero
                self.primero = self.primero.siguiente
                del aux
        return d
    
    def estaVacia(self):
        return self.primero==None and self.ultimo==None
    
    def liberaMemoria(self):
        while not self.estaVacia():
            print(self.pop())

if __name__ == '__main__':
    system('cls')

    C = Cola()

    for i in range(10):
        x = randrange(100)
        print(f'Se inserta {x}')
        C.push(x)

    print('\n\nFin del programa =)\n\nDestructor:')
