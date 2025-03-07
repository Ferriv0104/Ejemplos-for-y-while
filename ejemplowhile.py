# Cálculo de la altura promedio usando while
alturas_ninos = [155, 171, 148, 161, 158, 153, 162]
suma_alturas = 0
indice = 0

while indice < len(alturas_ninos):
    suma_alturas += alturas_ninos[indice]
    indice += 1

altura_promedio = suma_alturas // len(alturas_ninos)
print(f"La altura promedio es {altura_promedio}")

