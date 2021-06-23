from datetime import datetime
datos=[]

def menu():

    print('\n****************** MENU *****************')
    print('*\t                                *')
    print('*\t1. Registrar Partido            *')
    print('*\t2. Ver Resultados               *')
    print('*\t3. Tabla de Clasificacion       *')
    print('*\t4. Salir                        *')
    print('*\t                                *')
    print('*****************************************')


def datosPartido():
    #fecha = input('Ingrese la fecha dd-mm-yyyy: ')
    x='s'
    while x=='s':
        print('\n========================================\n')
        while True:
            try:
                fecha = input("Ingresa la fecha YYYY-MM-DD: ")
                datetime.strptime(fecha, '%Y-%m-%d')
                break
            except ValueError:
                print("Fecha inválida")

        nombreRival = input('Ingrese nombre equipo: ')
        golesRival = input(f'Digite numero de goles {nombreRival.upper()}: ')
        nombreLocal = 'UNAB'
        golesLocal = input(f'Digite numero de goles {nombreLocal}: ')
        print('\n========================================')

        datos.append((fecha, nombreRival.upper(), golesRival, nombreLocal, golesLocal))

        #print(datos)
        x = input('\nDesea agregar mas datos s/n: ')


def ordenarPorFecha():
    for i in range(1,len(datos)):
        x=datos[i]
        j=i-1
        while j>=0 and datos[j]>x:
            datos[j+1]=datos[j]
            j=j-1
        datos[j+1]=x
    return datos

def mostrarResultados():
    x = ordenarPorFecha()
    print('\n========================================')
    print('Fecha\t\tLocal\t   Visitante\n')
    print('\n'.join(i[0]+'\t'+i[3]+'('+str(i[4])+')\tVS ('+str(i[2])+')'+i[1] for i in x))
    print('\n========================================')


def tablaClasificacion():
    x = ordenarPorFecha()
    tabla=[]
    perdidos=0
    ganados=0
    empatados=0
    puntos=0
    cont=0
    pg=0
    pe=0
    for i in x:
        cont+=1
        if i[2] < i[4]:
            ganados+=1
            pg+=3
            print(perdidos)
        elif i[2] > i[4]:
            perdidos+=1
        elif i[2] == i[4]:
            empatados+=1
            pe+=1
    puntos=pg+pe
    tabla.append((cont, ganados, perdidos, empatados, puntos))
    print('\n================================================')
    print('EQUIPO\tPJ\tPG\tPP\tPE\tPUNTOS\n')
    print(f'UNAB\t{cont}\t{ganados}\t{perdidos}\t{empatados}\t{puntos}')
    print('\n================================================')



