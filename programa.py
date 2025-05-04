from os import system

def palindromoR(cadena, ini, fin):
    if cadena[ini] != cadena[fin]:
        return False
    elif ini<fin:
        palindromoR(cadena, ini+1, fin-1)
    return True

def esPalindromoR(cadena):
    editada = ''
    for caracter in cadena:
        if caracter.isalnum():
            editada += caracter.upper()

    return palindromoR(editada, 0, len(editada)-1)

if __name__ == '__main__':
    system('cls')

    cadena = input('Ingresa cadena ')

    if esPalindromoR(cadena):
        print('ES palíndromo =)')
    else:
        print('NO es palíndromo =(')
