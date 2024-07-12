import mysql.connector
try:
    #conexion con la BD de MYSQL
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
    )
except Exception as e:
    print(f"Error:{e}")
    print(f"tipo de error: {type(e)._name_}")
    print(f"Ocurrio un error por favor vuelva a intentar mas tarde ")    
else:       
    #verificar si la conexion es correcta 
    if conexion.is_connected():
        print(f"Se creo la conexion exitosamente")
    else:
     print(f"No fue posible conectar con la base de datos")