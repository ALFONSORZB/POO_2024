from conexionBD import*

try:
 micursor=conexion.cursor()
 sql="select * from clientes "


 micursor.execute(sql)

 resultado=micursor.fechall()
 for fila in resultado:
     print(f"id:{fila[0]} Nombre:{fila[1]} Direccion:{fila[2]} Tel:{fila[3]}")


except:
    print(f"Ocurrio un error por favor vuelva a intentar mas tarde...")
else:
    print(f"Registros consultados con exito")