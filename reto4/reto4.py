from reto4Fn import *

productos=[]


while True:
    menu()

    try:
        opcion=int(input("\nIngrese el numero de la opcion escogida: "))
        print()
    except:
        opcion=-1


    if opcion==1:
        crearProducto()
    elif opcion==2:
        buscarProducto()
    elif opcion==3:
        modificarPrecioCompra()
    elif opcion==4:
        modificarPrecioVenta()
    elif opcion==5:
        productoPorNombre()
    elif opcion==6:
        productoPorCompra()
    elif opcion==7:
        productoPorVenta()
    elif opcion==8:
        productoPorCantidad()
    elif opcion==9:
        mediaCompra()
    elif opcion==10:
        mediaVenta()
    elif opcion==11:
        eliminar()
    elif opcion==0:
        break
    else:
        print("La opcion ingresada es incorrecta, indica una opcion valida")




