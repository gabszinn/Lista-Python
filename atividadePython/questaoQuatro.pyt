distancia = float(input("Distância a percorrer (km): "))
velocidade_media = float(input("Velocidade média esperada (km/h): "))

tempo = distancia / velocidade_media
print(f"O tempo estimado de viagem é {tempo:.2f} horas")
