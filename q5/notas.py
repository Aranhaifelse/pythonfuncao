def media(notas):
    soma = 0
    quantidade = 0
    for i in notas:
        print(i)
        soma = soma + i
        quantidade = quantidade + 1
    resultado = soma / quantidade
    return resultado

def menor(notas):
    N_menor = notas[0]
    for i in notas:
        if N_menor > i: 
            N_menor = i 
    return N_menor

def maior(notas):
    N_maior = 0
    for i in notas:
        if N_maior < i:
            N_maior = i
    return N_maior