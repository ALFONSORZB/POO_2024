"""
Comentario de varias lineas
Nota: A la hora de concatenar cadenas, no es posible incluirt
en algunas ocasiones contenido de variables que no sean del tipo str 
"""

#Concatenar un str con str

numero=23
numero_str=str(numero)
print("El numero:"+numero_str)



print("El numero:" +str(numero))


#Concatenar un str con int

n1='23'
n2=33.0
suma=int(n1+n2)

print(f"El numero: {int(suma)}")

#Concatenar un float y float con float 

n1='23.34'
n2='33.99'
suma=int(n1+n2)

print(f"El numero: {suma}")
