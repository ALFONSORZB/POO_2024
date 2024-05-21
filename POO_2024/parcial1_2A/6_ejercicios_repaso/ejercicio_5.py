#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario
#Alfonso Ramirez Bravo
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
if num1 < num2:
    for i in range(num1, num2):
        print(i)
elif num1 > num2:
    for i in range(num2, num1):
        print(i)