def inverte_numero(numero):
    return int(str(numero)[::-1])

numero = int(input("Digite um número inteiro: "))
print(f"Número invertido: {inverte_numero(numero)}")
