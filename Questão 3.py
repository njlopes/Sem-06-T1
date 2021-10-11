def cor(n):
    if n.upper()=='V':
        return 'Siga'
    if n.upper()=='A':
        return 'Atenção'
    if n.upper()=='E':
        return 'Pare'

    
sinal = input('Digite V para verde, A para amarelo ou E para vermelho:)
resultado = cor(sinal)
print(resultado)

