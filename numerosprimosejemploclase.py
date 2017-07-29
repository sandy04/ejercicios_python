def es_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero % 2 == 0:
        return false
    else:
        for i in range (3,numero):
            if numero & i == 0:
                return False
    return True

    
def ejecutar():
    numero=int(input('Escribe un numero: '))
    resultado = es_primo(numero)

    if resultado is True:
        print('Tu numero es un numero primo')
    else:
        print('Tu número no es primo')

if __name__=='__main__':
    ejecutar()
