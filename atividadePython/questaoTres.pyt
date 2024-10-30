dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))

segundos = dias * 86400 + horas * 3600 + minutos * 60
print(f"Total de segundos: {segundos}")
