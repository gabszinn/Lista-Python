def conta_vogais(palavra):
    vogais = "aeiouAEIOU"
    contagem = sum(1 for letra in palavra if letra in vogais)
    return contagem

frase = input("Digite uma frase: ")
print(f"A palavra tem {conta_vogais(frase)} vogais")
