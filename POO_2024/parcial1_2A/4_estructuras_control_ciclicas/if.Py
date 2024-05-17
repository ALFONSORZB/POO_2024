#Existe una estructura de condicion llamada "if"
#La cual evalua una condicion para encontrar el valor "True" y si se cumple
#La condicion se eecuta la linea o lineas de codigo

#Tenes 4 variantes del if

#1.- If simple
#2.- if compuesto
#3.-
#4.-
#



        #Crear un programa que solocite el numero de la semaan que imprima en pantalla el dia que corresponde


def obtener_dia_de_la_semana(numero_de_semana):
    # Diccionario que asocia números con días de la semana
    dias_de_la_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    
    # Verificar que el número esté en el rango correcto
    if 1 <= numero_de_semana <= 7:
        return dias_de_la_semana[numero_de_semana]
    else:
        return "Número de semana inválido. Por favor, ingrese un número del 1 al 7."

# Solicitar al usuario el número de la semana
numero_de_semana = int(input("Ingrese el número de la semana (1-7): "))

# Obtener el día correspondiente
dia = obtener_dia_de_la_semana(numero_de_semana)

# Imprimir el día correspondiente
print(dia)
