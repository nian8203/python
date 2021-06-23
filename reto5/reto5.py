from procesos import*



while True:
    menu()

    try:
        opcion=int(input("\nIngrese una opcion: "))
        print()
    except:
        opcion=-1

    if opcion==1:
        datosPartido()
    elif opcion==2:
        mostrarResultados()
    elif opcion==3:
        tablaClasificacion()
    elif opcion==4:
        break
