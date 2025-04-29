from os import system

def funcionRecursiva(n):
    print(f'funcionRecursiva con n={n}')
    if n>1:
        funcionRecursiva(n-1)
    print(f'funcionRecursiva con n={n}')

if __name__ == '__main__':
    system('cls')

    funcionRecursiva(10)
