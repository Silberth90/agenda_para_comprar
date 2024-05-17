
def lista_que_falta():

# La lista vacio donde se van a guardar

    lista = []
    
    print("lista del supermercado")
    
    while True:
        print("\nLista de compras: ")
        for item in lista:
            print("- "+ item)
            
            # Le pide al usuario el articulo

        nuevo_item = input("\nIngrese el articulo que se agregara a la lista: ")

        if nuevo_item.lower() == "final":
            break


            # se genera la nueva lista

            
        lista.append(nuevo_item)
        print("Lo que hay que comprar en el supermercado es: ")
        
    print("\n!Lo que falta del supermercado! es: ")
    for item in lista:
        print("- "+item)

lista_que_falta()