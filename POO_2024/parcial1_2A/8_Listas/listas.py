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
    
    #Ejmeplo 2 crear una lista de palabras, posteriormente ingresar una palabra para buscar la concidencia en la lista
    #E indicar si aparece la palabra y en que posicion en caso contrario indicar una sola vez si no lo encontro.
    
palabras=("Hola","2024","10.23","True")

palabra_buscar=input("Ingresa la palabra a buscar: ")

for a in palabras:
    print(a)
    
    
    
    #Ejemplo 3 lista multimedia o multidimensional (matriz) para crear una agenda telefonica
    
    agenda=[
        ["Carlos",6181234567],
        ["Fernando",6182334567],
        ["Matias",6691112233],
        ["Juan Polainas",6182332345]
    ]
    
    print(agenda)
    
    for i in agenda:
        print(f"{agenda.index(i)+1}.-{i}")
        
        
        
        #Ejemplo 4 Crear un programa que permita gestionar (administrar) peliculas, colocar un menu de opciones
        #Para agregar, remover, consultar peliculas.
        #Notas:
        #1.-Utilizar funciones y mandar llamar desde otro archivo
        #2.-Utilizar listas para almacenar los nombres
        def insertarPeliculas():
            pelicula=input("Ingrese la pelicula: ")
            peliculas.append(Pelicula)
            espereTecla()
            
        def eliminarPeliculas():
            pelicula=input("Ingrese la pelicula: ")
            peliculas.remove(Pelicula)
            espereTecla()
            
            
            
            peliculas=[]
            
        print("\n\t..:::CINEPOLIS CLON:::,,\N 1.-Agregar  \n 2.-Eliminar \n 3.-Consultar \n 4.-SALIR")
        opcion=input("\t Elige una opcion: ").upper()
        
        if opcion=="1" or opcion=="AGREGAR":
            insertarPeliculas()
        elif opcion=="2" or opcion=="ELIMINAR":
            eliminarPeliculas()
            