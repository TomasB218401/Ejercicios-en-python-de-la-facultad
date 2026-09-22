# Ejercicio 1: Dada la siguiente información, elija una estructura de datos que permita guardarla 
# adecuadamente. 
# Guerra del Peloponeso 431 a.C  
# Revolución de Mayo 1810 d.C  
# Llegada de los españoles a América 1492 d.C  
# Comienzo de la construcción de la gran Muralla China 214 a.C

# Usaria un diccionario para guardar la informacion y buscarla despues por una key
# Crear la lista de diccionarios directamente
Hechos_historicos_lista = [
    {"Hecho": "Guerra del Peloponeso", "Fecha": "431 a.C"},
    {"Hecho": "Revolución de Mayo", "Fecha": "1810 d.C"},
    {"Hecho": "Llegada de los españoles a América", "Fecha": "1492 d.C"},
    {"Hecho": "Comienzo de la construcción de la Gran Muralla China", "Fecha": "214 a.C"}
]

# Recorrer la lista (sin paréntesis en el for)
for histo in Hechos_historicos_lista:
    print(f"Hecho: {histo['Hecho']}")
    print(f"Fecha: {histo['Fecha']}")
    print("-" * 20)

    