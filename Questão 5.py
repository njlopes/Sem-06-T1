def notas(x, y, z):
    nota1 = x
    nota2 = y
    nota3 = z
    media = (x+y+z) / 3
    if z >8:
        return media + 1
    else:
        return media
    if nota1 >= 8:
        print ('nota1 + 1')



n1 = int(input('Digite a nota 1:'))
n2 = int(input('Digite a nota 2:'))
n3 = int(input('Digite a nota 3:'))

if notas(n1, n2, n3) > 10:
    print ('10')
else:
    print (notas(n1, n2, n3))



