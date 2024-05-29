#Alfonso Ramirez  Bravo
tarifa_basica=.987  
tarifa_intermedia=1.203 
iva=.16  
impuesto=12.56 
kwh=150



if kwh <=(150):
        basico = kwh*tarifa_basica
        intermedio = 0
else:
        costo_B = 150*tarifa_basica
        costo_I = kwh-150*tarifa_intermedia
        
        costo_energia=tarifa_basica+tarifa_intermedia

    
iva=costo_energia*iva
total_pagar=costo_energia+iva+impuesto

    
print(f"Total a pagar: ${total_pagar}")
    
    
    
    
    
