from os import system

def potenciaRecursiva(a, b):
    # print(f'potenciaRecursiva({a}, {b})')
    if b>1:
        return a * potenciaRecursiva(a, b-1)
    else:
        return a

if __name__ == '__main__':
    system('cls')

    a = int(input('Ingresa a '))
    b = int(input('Ingresa b '))
    c = potenciaRecursiva(a, b)

    print(f'{a} ** {b} = {c}')
