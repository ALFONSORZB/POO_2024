#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado
# Alfonso Ramirez Bravo



num1 = input("Ingresa un numero: ")
num2 = input("Ingresa otro numero: ")

suma = int(num1) + int(num2)
resta = int(num1) - int(num2)
multi = int(num1) * int(num2)
division = int(num1) / int(num2)


print(f"La suma de los numeros es: {suma}")
print(f"La resta de los numeros es: {resta}")
print(f"La multiplicacion de los numeros es: {multi}")
print(f"La division de los numeros es: {division}")
