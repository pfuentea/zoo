from animal import *

class Zoo():
    def __init__(self):
        self.animales=[]

    def add_Washimingo(self,nombre):
        self.animales.append( Washimingo(nombre) )
        print(f'Washimingo {nombre} agregado!')
    
    def add_Centauro(self,nombre):
        self.animales.append( Centauro(nombre) )
        print(f'Centauro {nombre} agregado!')

    def add_Esfinge(self,nombre):
        self.animales.append( Esfinge(nombre) )
        print(f'Esfinge {nombre} agregada!')
    
    def add_Dragon(self,nombre):
        self.animales.append( Dragon(nombre) )
        print(f'Dragón {nombre} agregado!')

    def add_DragonM(self,nombre,material):
        self.animales.append(Dragon_Especial(nombre,material))
        print(f'Dragón {nombre} de {material} agregado!')

    def display_info(self):
        zoo=['ZOO->']
        for animal in self.animales:
            zoo.append('['+animal.Code()+']') 
        print('->'.join(zoo))
    def display_zoo(self):
        zoo=[]
        for i in range(len(self.animales)): #
            n=i+1
            zoo.append('['+str(n)+':'+self.animales[i].Code()+']') 
        print('-'.join(zoo))

    def interaccion(self,animal_index,accion):
        animal=animal_index-1    
        if accion =='1':
            self.animales[animal].alimentar()
        elif accion =='2':
            self.animales[animal].hidratar()
        elif accion =='3':
            self.animales[animal].display_info()
