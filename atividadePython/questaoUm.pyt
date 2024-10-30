nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

if idade > 18 and peso >= 60 and altura >= 1.70:
    print(f"Você está apto a servir o exército")
else:
    print(f"Você não está apto a servir o exército")
