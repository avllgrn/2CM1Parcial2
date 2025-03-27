from os import system

def esOperador(x):
    return x in {'+','-','*','/','//','%','^'}

def jerarquiaDe(operador):
    jerarquia = {'^':3, '*':2, '/':2, '//':2, '%':2, '+':1, '-':1}
    return jerarquia.get(operador)

if __name__ == '__main__':
    system('cls')

    expresion = input('Ingresa expresión ')
    print(expresion)
    lista = expresion.split()
    print(lista)

    for i in lista:
        if esOperador(i):
            print(f'{i} es operador con jerarquía {jerarquiaDe(i)}')
        else:
            print(f'{i} es operando')

# 1 - 2 + 9 * 7 / 8 % 3 // 8 ^ 2
