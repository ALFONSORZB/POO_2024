# List (Arrays)son colecciones o conjuntos de datos/valores bajo un mismo nombre, para acceder a los valores
#Se hace como un indice numerico    
#Nota: Sus valores si son modificable
#La lista es una coleccion ordenada y modificable. Permite miembros duplicados.



#Ejemplo 1 Crear una lista con valores numericos enteros e imprimir la lista

numeros=23
numeros=34

numeros=[23,34]
print(numeros)

#Recorrer la lista con un FOR
for i in numeros:
    print(i)
    
    
#Recorrer la lista con un WHILE
i=0
while i<len (numeros):
    print(numeros[i])
    i+=1
    