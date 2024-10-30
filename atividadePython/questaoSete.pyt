numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada do {numero}")
for i in range(10):
    print(f"{numero} X {i} = {numero * i}")
