from os import system

def multiplicacionRecursiva(a, b):
    # print(f'multiplicacionRecursiva({a}, {b})')
    if b>1:
        return a + multiplicacionRecursiva(a, b-1)
    else:
        return a

if __name__ == '__main__':
    system('cls')

    a = int(input('Ingresa a '))
    b = int(input('Ingresa b '))
    c = multiplicacionRecursiva(a, b)

    print(f'{a} * {b} = {c}')
