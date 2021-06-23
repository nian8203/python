def sumaLista(lista):
    num = 0
    suma = 0
    for num in lista:
        suma+=num
    return suma

def suma(num1, num2):
    res=num1+num2
    return res

def resta(num1, num2):
    res=num1-num2
    return res

def multi(num1, num2):
    res=num1*num2
    return res

def div(num1, num2):
    
    res=num1/num2
    return round(res,2)  

def llenarLista(lista):    

    veces = int(input('\nCuantos valores desea ingresar? '))
    print()

    for i in range(veces):
        num = int(input('Agregue un nuevo numero: '))
        lista.append(num)

    return lista

#================== funciones ejer menu 2 ========================

'''
def ingresarNombre(nombres):

    estado = 's'
    while estado == 's':
        nom = input('\nIngrese un nombre: ')
        nombres.append(nom)
        estado = input('Desea agregar otro estudiante? s/n: ')

    return nombres


    try:
        nom = input('Ingrese un nombre: ')
        nombres.append(nom)

    except:
        print('error')

    return nombres

def buscarEstudiante(lista):

    print(len(lista))

    opcion = 0
    nombre  = input('Ingrese el nombre del alumno: ')
    for i in lista:
        if nombre == i:
            #print('El alumno ',str(i),'se encuentra registrado')
            opcion = 1
            break
        else:
            opcion = 0
            break

    return opcion

'''

def menu():

    print('\n******************** MENU ******************')
    print('*\t                                   *')
    print('*\t1. Agregar estudiante              *')
    print('*\t2. Buscar estudiante               *')
    print('*\t3. Modificar nota                  *')
    print('*\t4. Estudiantes orden por nombre    *')
    print('*\t5. Estudiantes orden por nota      *')
    print('*\t6. Promedio notas                  *')
    print('*\t7. Eliminar estudiante             *')
    print('*\t8. Salir                           *')
    print('*\t                                   *')
    print('********************************************')


def entrarNombre():
    while True:
        nombre = input('ingrese el nombre del estudiante a agregar: ')
        if nombre =='':
            print('Debe ingresar un nombre...')
        else:
            return nombre

def entrarNota():
    while true:
        try:
            nota = float(input('Ingrese la nota del estudiante (0-10): '))
            if 0 <= nota <=10:
                return nota
            else:
                print('la nota debe estar entre 0 y 10')


def buscarEstudiante():
    nombre = entrarNombre()
    for alumn in estudinates:
        if alum[0]==nombre:
            print("La nota del estudiante '{}' es {}".format(nombre, alum[1]))
            return True
    print('No se encuentra el estudiante')
    return false

def buscar(nombre):
    for i,e in enumerate(estudinates):
        if e[0]==nombre:
            return i
    return -1


def modificarNota():
    nombre = input('ingrese el numero del estudiante a buscar: ')
    indice=buscar(nombre)
    if indice==-1:
        print('No se ha encontrado el estudinate '{}.format(nombre)) #"hola'{}'".format
        return false
    tmp=list(estudinates[indice])
    tmp[1]=entrarNota()
    estudinates[indice]=tuple(tmp)
    print("Se ha actualizado la nota al estudiante '{}'".format(nombre))
        

def listarEstudianteNombre():
    estudiantes.sort()
    print("\n".join(i[0]+" - "+str(i[1]) for i in estudinates))

def listarEstudianteNota():
    estudiantes.sort(key=lambda.x: x[1], reverse=True)
    print("\n".join(i[0]+" - "+str(i[1]) for i in estudiantes))

def notaPromedio():
    if len(estudiantes)==0:
        print("No hay datos registrados")
        return false
    promedio=sum([i[1] for i in estudiantes])/len(estudiantes)
    print("La nota promedio de", len(estudiantes), "estudinates es '{}'".format(promedio))

def borrarEstudiante():
    nombre=input("Inrese el nombre del estudiante: ")
    indice=buscar(nombre)
    if indice==-1:
        print("El registro con el nombre '{}' no se a encontrado".format(nombre))
        return false
    print("Se a eliminado el registro con el nombre '{}' con la nota {}".format(nombre, estudiantes[indice][1]))#el primero en comilla sencilla
    #por que es str y en el format se le pasan los parametros que queremos mostrar
    del estudiantes[indice]
    return true




