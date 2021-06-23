from zoologico import Zoo

def menu_animales():
    print("[1]:Washimingo")
    print("[2]:Centauro")
    print("[3]:Esfinge")

def valida_interactuar(z,indice):
    
    if indice =='x':
        return 0
    else:
        indice=int(indice)
        if(indice>0 and indice <= len(z.animales)):
            return indice
        else:
            return 0

def menu_interaccion():
    print("[1]:Alimentar [2]:Hidratar [3]: Ver Info")

z=Zoo()
continuar=True
print("Bienvenido al Zoo!")
print("Que desea hacer?:")
while(continuar):
        opt1=input("[1]:Agregar especie \n[2]:Interactuar con animal  \n[3]:Salir \n Opcion?:")
        if opt1=='1':
            continuar_menu1=True
            while(continuar_menu1):
                print("Que especie desea agregar?:")
                menu_animales()
                opt2=input("Seleccione una especie (x=Volver menú anterior):")
                if opt2=='1':
                    nombre=input("Ingrese un nombre para el Washimingo:")
                    z.add_Washimingo(nombre)
                    continuar_menu1=False
                elif opt2=='2':
                    nombre=input("Ingrese un nombre para el Centauro:")
                    z.add_Centauro(nombre)
                    continuar_menu1=False
                elif opt2=='3':
                    nombre=input("Ingrese un nombre para la Esfinge:")
                    z.add_Esfinge(nombre)
                    continuar_menu1=False
                elif opt2=='x':
                    continuar_menu1=False    
                else:
                    print ("Ese animal aún no lo traemos. Vuelva a intentar")
            
        if opt1=='2':
            continuar_menu2=True
            while(continuar_menu2):
                if len(z.animales)>0:
                    z.display_zoo()
                    interactuar=input("Con que animal desea interactuar?(x=volver al menu anterior):")
                    indice_correcto=valida_interactuar(z,interactuar)
                    #validamos si el indice es correcto o si no preguntamos de nuevo
                    if(indice_correcto>0):
                        z.animales[indice_correcto-1].display_corto()
                        menu_interaccion()
                        accion=input("Elija una opción:")
                        resultado=z.interaccion(indice_correcto,accion)
                    else:
                        continuar_menu2=False
                else:
                    print("Aún no existen animales, deberías agregar algunos!")
                    continuar_menu2=False



        if opt1=='3':
            continuar=False
        print('El Zoo está conformado de la siguiente forma:')
        z.display_info()

print('Gracias por visitar el Zoo!')