# Questão 1 - Manipulação de listas e strings

def quantificador (word, phrase):
    frase_minuscula = phrase.lower()
    palavra_minuscula = word.lower()
    palavras_frase = frase_minuscula.split()
    quantidade = 0
    for p in palavras_frase:
        if p == palavra_minuscula:
            quantidade += 1
    return quantidade

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar: ")

quantidade = quantificador(palavra, frase)

# Quantidade de Palavras
print(quantidade)
