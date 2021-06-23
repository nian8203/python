productos=[]

def menu():
    print('\n******************** MENU *************************')
    print('*\t                                          *')
    print('*\t1. Añadir producto                        *')
    print('*\t2. Buscar producto                        *')
    print('*\t3. Modificar precio compra                *')
    print('*\t4. Modificar precio venta                 *')
    print('*\t5. Listar por nombre                      *')
    print('*\t6. Listar por precio compra               *')
    print('*\t7. Listar por precio venta                *')
    print('*\t8. Listar por cantidad                    *')
    print('*\t9. Promedio productos por precio compra   *')
    print('*\t10. Promedio productos por precio venta   *')
    print('*\t11. Borar producto                        *')
    print('*\t0. Salir                                  *')
    print('*\t                                          *')
    print('***************************************************')



def agregarProducto():
    producto = input('Ingrese el nombre del producto: ')
    return producto
    while producto == "":
        producto = input('Debe ingresar el nombre del producto: ')



def valorCompra():
    x = 0
    while x == 0:
        try:
            precioCompra = float(input('Digite el valor de compra: '))
            return precioCompra
            while precioCompra == "":
               precioCompra = float(input('Debe ingresar un valor de compra: '))
            x = 1


        except:
            print('--- debe ingresar solo valores numericos ---')



def valorVenta():
    x = 0
    while x == 0:
        try:
            precioVenta = float(input('Digite valor de venta: '))
            return precioVenta
            while precioVenta == "":
                precioVenta = float(input('Debe ingresar un valor de venta: '))
            x = 1
        except:
            print('--- debe ingresar solo valores numericos ---')

def cantidadProducto():
    x = 0
    while x == 0:
        try:
            cantidad = int(input('Digite la cantidad: '))
            return cantidad
            while cantidad == '':
                cantidad = int(input('Debe ingresar la cantidad: '))
        except:
            print('--- debe ingresar solo valores numericos ---')


def crearProducto():
    productos.append((agregarProducto(), valorCompra(), valorVenta(), cantidadProducto()))
    print('\nProducto creado con exito!!!\nNombre:\t',productos)


def buscarProducto():
    producto = input('Ingrese el nombre del producto: ')
    for p in productos:
        if p[0] == producto:
            print("El producto se encuentra registrado\nNombre = '{}' \nValor compra = {}\nValor venta = {}\nCantidad = {}".format(producto, p[1], p[2], p[3]))
            return True
    print("Producto no encontrado")
    return False



def modificarPrecioCompra():
    n = 'nuevo'
    producto = input('Ingrese el nombre del producto: ')
    posicion = buscarPosicion(producto)
    if posicion != -1:
        tmp = list(productos[posicion])
        tmp[1] = valorCompra()
        productos[posicion]=tuple(tmp)
        print("El '{}' valor de compra del producto '{}' se ha sido actualizada".format(n, producto))
        return True
    else:
        print('El producto no se encuentra registrado')
        return False

def modificarPrecioVenta():
    n = 'nuevo'
    producto = input('Ingrese el nombre del producto: ')
    posicion = buscarPosicion(producto)
    if posicion != -1:
        tmp = list(productos[posicion])
        tmp[2] = valorCompra()
        productos[posicion]=tuple(tmp)
        print("El '{}' valor de venta del producto '{}' se ha sido actualizado".format(n, producto))
        return True
    else:
        print('El producto no se encuentra registrado')
        return False


def productoPorNombre():
    productos.sort()
    print('Nombre\tCompra\tVenta\tCantidad')
    print('\n'.join(i[0]+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3]) for i in productos))
    return True


def productoPorCompra():
    productos.sort(key=lambda x: x[1], reverse=True)
    print('Nombre\tCompra\tVenta\tCantidad')
    print('\n'.join(i[0]+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3]) for i in productos))
    return True

def productoPorVenta():
    productos.sort(key=lambda x: x[2], reverse=True)
    print('Nombre\tCompra\tVenta\tCantidad')
    print('\n'.join(i[0]+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3]) for i in productos))
    return True


def productoPorCantidad():
    productos.sort(key=lambda x: x[3], reverse=True)
    print('Nombre\tCompra\tVenta\tCantidad')
    print('\n'.join(i[0]+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3]) for i in productos))
    return True

def mediaCompra():
    cont = 0
    s = 0
    for i in productos:
        s+=i[1]
        cont +=1
        media = s/cont
    print('Producto\tValor compra')
    print('\n'.join(i[0]+'\t\t'+str(i[1]) for i in productos))
    print("\nEl promedio del precio de compra es ${}".format(int(media)))


def mediaVenta():
    cont = 0
    s = 0
    for i in productos:
        s+=i[2]
        cont +=1
        media = s/cont
    print('Producto\tValor compra')
    print('\n'.join(i[0]+'\t\t'+str(i[2]) for i in productos))
    print("\nEl promedio del precio de compra es ${}".format(int(media)))


def eliminar():
    producto = input('Ingrese el nombre del producto: ')
    posicion = buscarPosicion(producto)
    if posicion != -1:
        print("El producto '{}' se ha sido eliminado".format(producto))
        del productos[posicion]
        return True
    else:
        print("El producto '{}' no se encuentra registrado".format(producto))


def buscarPosicion(producto):
    for i,e in enumerate(productos):
        if e[0] == producto:
            return i
    return -1









