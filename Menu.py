while True: 
        print(" MENU \n 1. Personas \n 2. Vehiculos \n 3. Universidades \n 4.Notas \n 5. Salir ")
        opcion = int (input("Seleccione una opcion: "))


        if opcion>5 or opcion <1:
            print("La opcion no existe")
            
        elif opcion == 1:
            print("Hola has presionado la opcion Personas")
            
        elif opcion == 2:
            print("Hola has presionado la opcion Vehiculos")
            
        elif opcion == 3:
            print("Hola has presionado la opcion Universidades")
        
        elif opcion == 4:
            print("Hola has presionado la opcion Notas")
            
        elif opcion == 5:
            print("Gracias por usar nuestra app")
            break
    
