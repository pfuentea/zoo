from zoologico import Zoo

def menu_animales():
    print("[1]:Washimingo")
    print("[2]:Centauro")
    print("[3]:Esfinge")
    print("[4]:Dragón")
    print("[5]:Dragón Especial")

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
print("Que desea hacer?: ")
while(continuar):
    opt1=input("[1]:Agregar especie \n[2]:Interactuar con animal  \n[3]:Salir \n Opcion?: ")
    if opt1=='1':
        while(True):
            print("Que especie desea agregar?: ")
            menu_animales()
            opt2=input("Seleccione una especie (x=Volver menú anterior): ")
            if opt2=='1':
                nombre=input("Ingrese un nombre para el Washimingo: ")
                z.add_Washimingo(nombre)
                break
            elif opt2=='2':
                nombre=input("Ingrese un nombre para el Centauro: ")
                z.add_Centauro(nombre)
                break
            elif opt2=='3':
                nombre=input("Ingrese un nombre para la Esfinge: ")
                z.add_Esfinge(nombre)
                break
            elif opt2=='4':
                nombre=input("Ingrese un nombre para el Dragón: ")
                z.add_Dragon(nombre)
                break
            elif opt2=='5':
                nombre=input("Ingrese un nombre para el Dragón: ")
                material=input("Ingrese un material para el Dragón: ")
                z.add_DragonM(nombre,material)
                break
            elif opt2=='x':
                break
            else:
                print ("Ese animal aún no lo traemos. Vuelva a intentar.")
        
    if opt1=='2':
        while(True):
            if len(z.animales)>0:
                z.display_zoo()
                interactuar=input("Con que animal desea interactuar?(x=volver al menu anterior): ")
                indice_correcto=valida_interactuar(z,interactuar)
                if(indice_correcto>0):
                    z.animales[indice_correcto-1].display_corto()
                    menu_interaccion()
                    accion=input("Elija una opción: ")
                    resultado=z.interaccion(indice_correcto,accion)
                else:
                    print("Opción no valida, vuelva a intentar.")
                    break
            else:
                print("Aún no existen animales, deberías agregar algunos! ")
                break
    if opt1=='3':
        x=input("Ingrese x si esta seguro que desea salir o ENTER para continuar: ")
        if x=='x':
            break
    print('El Zoo está conformado de la siguiente forma: ')
    z.display_info()

print('Gracias por visitar el Zoo!')