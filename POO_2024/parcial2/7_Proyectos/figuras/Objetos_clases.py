class figuras:
    def __int__(self,calcularArea):
        self.calcularAera=calcularArea
        
    atributo_publico="Soy un atributo publico"
    atributo_privado="Soy un atributo privado"
    
    def MetodoPublico(self):
     return self.__atributo_privado
 
    def calcularArea(self):
     pass
 
 
class rectangulo(figuras):
    def getlargo(self):
        return self.largo
    
    def getancho(self):
        return self.ancho
    
    def get__int__(self,largo,ancho):
     self.largo=largo
     self.amcho=ancho
     
    def getcalcularArea(self):
        return self.largo*self.ancho
    
    def getInfo(Self):
     print(f"Rectángulo de largo {Self.largo}, ancho {Self.ancho} y área {Self.calcular_area()}")
    
    class circulo(figuras):
        def get__int__(self,radio):
            self.radio=radio
            
        def calcularArea(Self):
          return 3.14*Self.radio**2
      
        def getradio(self):
            return self.radio
        
        def setradio(Self,radio):
            self.radio=radio
            
        def getInfo(self):
            print(f"Círculo radio{self.radio} y área{self.calcular_area()}")
            
            
    class Triangulo(figuras):
     def get__init__(self, altura, ancho):
        self.altura=altura
        self.ancho=ancho

    def calcular_area(self):
        return 0.5*self.ancho*self.altura

    def getAltura(self):
        return self.altura

    def setAltura(self,altura):
        self.altura=altura

    def getAncho(self):
        return self.ancho

    def setAncho(self,ancho):
        self.ancho=ancho

    def getInfo(self):
        print(f"Triángulo medida de altura{self.altura}, ancho{self.ancho} y área{self.calcular_area()}")

    
    
    