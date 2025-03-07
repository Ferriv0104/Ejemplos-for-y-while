#EJEMPLO DE FOR 
alturas_ninos = [160, 171, 148, 161, 158, 153, 162]
suma_alturas = 0

for altura in alturas_ninos:
    suma_alturas = suma_alturas + altura

altura_promedio = suma_alturas // len(alturas_ninos)
print(altura_promedio)
