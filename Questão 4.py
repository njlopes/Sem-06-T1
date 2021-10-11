def numeros(x):
    if x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return print('True')
  
    else:
        print('False')


def main():
    valor = input('Digite um valor numérico:').lower()
    n = numeros(valor)


if __name__=='__main__':
    main()
