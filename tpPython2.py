# """ Ejercicio 2: Asígneles a las variables num1 y num2 los distintos valores indicados en la tabla.
# Realice las siguientes cuentas con las operaciones indicadas almacenando el resultado en la
# variable resul. En la tabla que aparece a continuación coloque los resultados obtenidos y
# justifíquelo. """

#intentando aplicar POO


# """ # Atributos
# Lista_NumValores1y2 = [
#     {"num1": 0, "num2": 0}
# ]

# Signos_Aritmeticos = [
#     {"Suma": "+", "Resta": "-", "Multiplicación": "*", "División": "/"}
# ]

# #funciones
# def ProcesarNumeros(listanum1y2):
#     for i in range(len(listanum1y2)):
#         num1 = float(input("Ingrese el primer valor: "))
#         listanum1y2[i]["num1"] += num1
#         num2 = float(input("Ingrese el segundo valor: "))
#         listanum1y2[i]["num2"] += num2
# #Final de la función
    
# def CalcularResultados(listanum1y2, signos):
#     for i in range(len(listanum1y2)):
#         num1 = listanum1y2[i]["num1"]
#         num2 = listanum1y2[i]["num2"]
#         resul_suma = num1 + num2
#         resul_resta = num1 - num2
#         resul_multiplicacion = num1 * num2
#         resul_division = num1 / num2 if num2 != 0 else "Indefinido (división por cero)"
        
#         print(f"Resultados para los números {num1} y {num2}:")
#         print(f"Suma: {resul_suma}")
#         print(f"Resta: {resul_resta}")
#         print(f"Multiplicación: {resul_multiplicacion}")
#         print(f"División: {resul_division}")
#         print("-" * 20)


# #def calculo_de_dos_numerosReales(listaNum,ListaSignos):
    
# #testeo final de las funciones
# ProcesarNumeros(Lista_NumValores1y2)

# CalcularResultados(Lista_NumValores1y2, Signos_Aritmeticos)  """


# """ Ejercicio 2: Asígneles a las variables num1 y num2 los distintos valores indicados en la tabla.
# Realice las siguientes cuentas con las operaciones indicadas almacenando el resultado en la
# variable resul. En la tabla que aparece a continuación coloque los resultados obtenidos y
# justifíquelo. """
# Atributos
Lista_NumValores1y2 = []

def ProcesarDatos(Lista):
    for i in range(6):
        print(f"\n--- Fila {i+1} de 6 ---")
        num1 = input("Ingrese un dato para num1: ")
        num2 = input("Ingrese un dato para num2: ")
      
        Lista.append({"num1": num1, "num2": num2})
# Fin de la funcion

def CalcularResultados(Lista):
    for i in range(len(Lista)):
        # 1. Evaluamos y convertimos cada variable por separado a int
        if Lista[i]["num1"].isdigit():
            num1 = int(Lista[i]["num1"])
        else:
            num1 = Lista[i]["num1"]
            
        if Lista[i]["num2"].isdigit():
            num2 = int(Lista[i]["num2"])
        else:
            num2 = Lista[i]["num2"]
        
        print(f"\n--- Valores actuales: '{num1}' (Tipo: {type(num1).__name__}) y '{num2}' (Tipo: {type(num2).__name__}) ---")
        print("¿Qué desea hacer con estos números?")
        print("Opciones: + (sumar/concatenar), - (restar), * (multiplicar/repetir), / (dividir), // (división entera)")
        operacion = input("Ingrese el símbolo de la operación: ")
        
        try:
            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                resultado = num1 / num2 if num2 != 0 else "Indefinido (división por cero)"
            elif operacion == "//":
                resultado = num1 // num2 if num2 != 0 else "Indefinido (división por cero)"
            else:
                resultado = "Operación no reconocida."
            
            print(f"Resultado de la operación: {resultado}")
            print("-" * 20)
            
        except TypeError:
            print("Error: No es posible realizar esa operación con la combinación de datos ingresada (ej. restar letras).")
            print("-" * 20)
# Fin de la funcion

# MAIN
ProcesarDatos(Lista_NumValores1y2)
CalcularResultados(Lista_NumValores1y2)

print("\nTabla final de datos:")
for fila in Lista_NumValores1y2:
    print(fila)