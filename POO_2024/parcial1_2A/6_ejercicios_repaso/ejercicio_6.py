#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
#Alfonso Ramirez Bravo
def tablas():
    for i in range(1, 11):  
        print(f"Tabla del {i}")
        for n in range(1, 11):  
            print(f"{i} x {n} = {i * n}")
        print()  
tablas()
