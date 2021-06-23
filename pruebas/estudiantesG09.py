#Uso de listas con estudiantes con un menu


def entrarNombre():
    """ Funcion para añadir un nombre """
    while True:
        nombre=input("Ingrese el nombre del estudiante a añadir: ")
        if nombre=="":
            print("El nombre no puede estar vacio")
        else:
            return nombre

def entrarNota():
    """ Funcion para añadir una nota """
    while True:
        try:
            nota=float(input("Ingrese la nota del estudiante (0-10): "))
            if 0<=nota<=10:
                return nota
            else:
                print("La nota tiene que estar entre 0 y 10")
        except:
            print("La nota tiene que ser un valor numerico")

def entrarMateria():
    while True:
        materia=input("Ingrese el nombre de la materia a añadir: ")
        if materia=="":
            print("La materia no puede estar vacio")
        else:
            return materia


def buscarEstudiante():
    nombre=input("Ingrese el nombre del estudiante a buscar: ")
    for alum in estudiantes:
        if alum[0]==nombre:
            print("La nota del estudiante '{}' es {}".format(nombre, alum[1]))
            return True
    print("No se encuentra el estudiante")
    return False

def buscar(nombre):
    for i,e in enumerate(estudiantes):
        if e[0]==nombre:
            return i
    return -1

def modificarNota():
    nombre=input("Ingrese el nombre del estudiante a buscar: ")
    indice=buscar(nombre)
    if indice==-1:
        print("No se ha econtrado el estudiante '{}'".format(nombre))
        return False
    tmp=list(estudiantes[indice])
    tmp[1]=entrarNota()
    estudiantes[indice]=tuple(tmp)
    print("Se ha actualizado la nota al estudiante '{}'".format(nombre))
    return True

def listarEstudiantesNombre():
    estudiantes.sort()
    print("\n".join(i[0]+" - "+str(i[1])+" - "+i[2] for i in estudiantes))
    return True

def listarEstudiantesNota():
    estudiantes.sort(key=lambda x: x[1], reverse=True)
    print("\n".join(i[0]+" - "+str(i[1]) for i in estudiantes))
    return True

def listarEstudiantesMateria():
    estudiantes.sort(key=lambda x: x[2], reverse=True)
    print("\n".join(i[0]+" - "+str(i[1])+" - "+i[2] for i in estudiantes))
    return True

def  notaPromedio():
    if len(estudiantes)==0:
        print("En la lista no hay estudiantes registrados")
        return False
    promedio=sum([i[1] for i in estudiantes])/len(estudiantes)
    print("La nota promedio de", len(estudiantes), "estudiantes es '{}'".format(round(promedio,1)))

def borrarEstudiante():
    nombre=input("Ingrese el nombre del estudiante a buscar: ")
    indice=buscar(nombre)
    if indice==-1:
        print("No se ha encotrado el estudiante '{}'".format(nombre))
        return False
    print("Se ha eliminado el estudiante '{}' con nota {}".format(nombre, estudiantes[indice][1]))
    del estudiantes[indice]
    return True


def menu():
    print('\n******************** MENU ******************')
    print('*\t                                   *')
    print('*\t1. Agregar estudiante              *')
    print('*\t2. Buscar estudiante               *')
    print('*\t3. Modificar nota                  *')
    print('*\t4. Estudiantes orden por nombre    *')
    print('*\t5. Estudiantes orden por materia   *')
    print('*\t6. Estudiantes orden por nota      *')
    print('*\t7. Promedio notas                  *')
    print('*\t8. Eliminar estudiante             *')
    print('*\t0. Salir                           *')
    print('*\t                                   *')
    print('********************************************')


#definimos la lista que contendra a cada estudiante
estudiantes=[]

while True:
    menu()

    try:
        opcion=int(input("\nIngrese el numero de la opcion escogida: "))
        print()
    except:
        opcion=-1

    if opcion==1:
        estudiantes.append((entrarNombre(), entrarNota(), entrarMateria()))
        print(estudiantes)
    elif opcion==2:
        buscarEstudiante()
    elif opcion==3:
        modificarNota()
    elif opcion==4:
        listarEstudiantesNombre()
    elif opcion==5:
        listarEstudiantesMateria()
    elif opcion==6:
        listarEstudiantesNota()
    elif opcion==7:
        notaPromedio()
    elif opcion==8:
        borrarEstudiante()
    elif opcion==0:
        break
    else:
        print("La opcion ingresada es incorrecta, indica una opcion valida")

