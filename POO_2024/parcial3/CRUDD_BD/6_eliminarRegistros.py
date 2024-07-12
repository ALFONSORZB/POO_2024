from conexionBD import*

try:
 micursor=conexion.cursor()
 sql="select * from clientes "


 micursor.execute(sql)
 sql="delete from clientes where id=1"
 
 
 micursor.execute(sql)
 #Es necesario ejecutar el commit para que finalice el SQL con exito
 conexion.commit()

except:
    print(f"Ocurrio un error por favor vuelva a intentar mas tarde...")
else:
    print(f"Registro eliminado con exito")