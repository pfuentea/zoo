class Animal():
    def __init__(self, nombre,edad,felicidad,salud,codigo):
        self.nombre=nombre
        self.edad=edad
        self.felicidad=felicidad
        self.salud=salud
        self.codigo=codigo

    def alimentar(self):
        raise NotImplementedError

    def hidratar(self):
        raise NotImplementedError

    def display_info(self):
        raise NotImplementedError
    
    def Code(self):
        return self.codigo
    
    def display_corto(self):
        raise NotImplementedError

class Washimingo(Animal):
    def __init__(self,nombre):
        super().__init__(nombre,0,20,20,'WSH')
        self.colas=2        

    def alimentar(self):
        self.salud+=2
        self.felicidad+=2
        print("Gracias por alimentarlo. Ha ganado +2 de salud y +2 de felicidad.")
        return self

    def hidratar(self):
        self.salud+=2
        self.felicidad+=2
        print("Gracias por darle de beber. Ha ganado +2 de salud y +2 de felicidad.")
        return self

    def display_info(self):
        print (f"El Washimingo {self.nombre} de edad {self.edad} tiene {self.salud} puntos de salud y {self.felicidad} puntos de felicidad. Mueve sus {self.colas} colas de un lado a otro.")
        return self

    def display_corto(self):
        print(f"Acá está {self.nombre} el Washimingo acicalandose...")
        return self

class Centauro(Animal):
    def __init__(self,nombre):
        super().__init__(nombre,0,20,20,'CNT')
        self.velocidad=40        

    def alimentar(self):
        self.salud+=5
        self.felicidad+=5
        print("Gracias por alimentarlo. Ha ganado +5 de salud y +5 de felicidad.")
        return self
    
    def hidratar(self):
        self.salud+=5
        self.felicidad+=5
        print("Gracias por darle de beber. Ha ganado +5 de salud y +5 de felicidad.")
        return self
    
    def display_info(self):
        print (f"El Centauro {self.nombre} de edad {self.edad} tiene {self.salud} puntos de salud y {self.felicidad} puntos de felicidad. Puede correr a {self.velocidad} km/h.")
        return self

    def display_corto(self):
        print(f"Acá está {self.nombre} el centauro ignorandote...")
        return self
    
class Esfinge(Animal):
    def __init__(self,nombre):
        super().__init__(nombre,0,20,20,'SPX')
        self.acertijos=3        

    def alimentar(self):
        self.salud+=10
        self.felicidad+=10
        print("Gracias por alimentarlo. Ha ganado +10 de salud y +10 de felicidad.")
        return self
    
    def hidratar(self):
        self.salud+=10
        self.felicidad+=10
        print("Gracias por dar de beber. Ha ganado +10 de salud y +10 de felicidad.")
        return self
    
    def display_info(self):
        print (f"La esfinge {self.nombre} de edad {self.edad} tiene {self.salud} puntos de salud y {self.felicidad} puntos de felicidad. Tiene {self.acertijos} para tí.")
        return self

    def display_corto(self):
        print(f"Acá está {self.nombre} la esfinge mirandote...")
        return self    
        
class Dragon(Animal):
    def __init__(self,nombre):
        super().__init__(nombre,0,20,20,'DRG')
        self.dientes=500        

    def alimentar(self):
        self.salud+=1
        self.felicidad+=1
        print("Gracias por alimentarlo. Ha ganado +1 de salud y +1 de felicidad.")
        return self
    
    def hidratar(self):
        self.salud+=1
        self.felicidad+=1
        print("Gracias por dar de beber. Ha ganado +1 de salud y +1 de felicidad.")
        return self
    
    def display_info(self):
        print (f"El dragón {self.nombre} de edad {self.edad} tiene {self.salud} puntos de salud y {self.felicidad} puntos de felicidad. Te muestra sus {self.dientes} dientes cuando te acercas.")
        return self

    def display_corto(self):
        print(f"Acá está {self.nombre} el dragón escudriñandote...")
        return self

class Material():
    def __init__(self,tipo):
        self.tipo=tipo

class Dragon_Especial(Dragon,Material):
    def __init__(self, nombre,material):
        Dragon.__init__(self,nombre)
        Material.__init__(self,material)
        self.codigo='SP-DRG'

    def display_info(self):
        print (f"El Dragón {self.nombre} de {self.tipo}, con edad {self.edad} tiene {self.salud} puntos de salud y {self.felicidad} puntos de felicidad. Tiene sus {self.dientes} dientes de {self.tipo} listos para usarlos.")
        return self
