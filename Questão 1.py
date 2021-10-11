def sexo(n):
    if n == 1:
        return 'Ilmo Sr.'
    elif n == 2:
        return 'Ilma Sra.'

nome = input('Digite seu nome:')
inf_sex = int(input('Digite seu sexo (1 = masculino; 2 = feminino):'))
resultado = sexo(inf_sex)
print(f'{resultado} {nome}')




           

