#Manejo de errores es la forma en la que tienen los lenguajes de programacion
#Para evitar que sucedan errores en tiempo de ejecucion

#Ejemplo 1 Error cuando una variable no se genera

try: 
     nombre=input("Dame el nombre: ")

     if len(nombre)>=1:
      nombre_usuario="El nombre es "+nombre
      print(nombre_usuario)
    
except:
 print("Es necesario introducir un nombre de usuario...")
    
    

    #Ejemplo 2 Cuando se solicita un numero y se introduce una letra
try:
     numero=(input("Dame un numero: "))
     if numero>0:              
      print("Soy un numero entero positivo")
     else:
      print("Soy un numero entero negativo")
except:
      print("No se puede convertir un caracter ")  
else: 
     print("Todo se ejecuto sin errores")
     
     #Ejemplo 3 cuando se generan multiples excepciones
     try:
       numero=int(input("Dame un numero: "))
     
       print("El cuadrado es: "+str(numero*numero))
     except ValueError:
          print("Debes introducir un numero, no se puede convertir un caracter que no sea numerico")
     except TypeError:
          print("No es posible convertir el numero a entero")
     else:
          print("Finalizo correctamente")
     finally:
          print("Listo se termino")
               
     
     
     
     #ValueError