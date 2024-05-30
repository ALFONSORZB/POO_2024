print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
print("5.- Salir")
opcion=input("\t Elige una opcion: ").upper()

n1=int(input("Numero # 1:"))
n2=int(input("Numero # 2:"))
if opcion=="1" or opcion=="+" or opcion=="SUMA":
        suma=n1+n2
        print(f"{n1}+{n2}={suma}")
elif opcion=="2" or opcion=="-" or opcion=="RESTA":
 resta=n1+n2
 print(f"{n1}+{n2}={resta}")
elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":       
 multiplicacion=n1+n2
 print(f"{n1}+{n2}={multiplicacion}")
elif opcion=="4" or opcion=="/" or opcion=="DIVISION":       
 division=n1+n2
 print(f"{n1}+{n2}={division}")
else:
    print("Gracias por utilizar el sistema...")