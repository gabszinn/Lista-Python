valor_casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Quantos anos para pagar: "))

prestacao_mensal = valor_casa / (anos * 12)

if prestacao_mensal > 0.3 * salario:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
