from os import system

def fibonacci(n):
    # print(f'fibonacci({n})')
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    system('cls')

    n = int(input('Ingresa n '))
    f = fibonacci(n)

    print(f'fibonacci(n) = {f}')
