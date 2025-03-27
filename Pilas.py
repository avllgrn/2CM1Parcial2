from os import system
from random import randrange

class Nodo:
    def __init__(self, dato=None, inferior=None):
        self.dato = dato
        self.inferior = inferior

    def __str__(self):
        cadena = '| ' + str(self.dato) + ' |'

        if self.inferior != None:
            cadena += ' -> '
        
        return cadena
    
class Pila:
    def __init__(self):
        self.tope = None

    def __del__(self):
        self.liberaMemoria()

    def push(self, d):
        self.tope = Nodo(d, self.tope)

    def pop(self):
        d = None
        if not self.estaVacia():
            d = self.tope.dato
            aux = self.tope
            self.tope = self.tope.inferior
            del aux
        return d
    
    def estaVacia(self):
        return self.tope == None
    
    def liberaMemoria(self):
        while not self.estaVacia():
            print(self.pop())

if __name__ == '__main__':
    system('cls')

    P = Pila()

    for i in range(10):
        x = randrange(100)
        print(f'Se inserta {x}')
        P.push(x)

    print('\n\nFin del programa =)\n\nDestructor:')
