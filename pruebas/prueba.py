'''crubio240@unab.edu.co //correo por alguna info'''

"""
a='Bucaramanga'
ini=2
fin=6
subcadena=a[ini:fin]
print(subcadena)

print(a[6:11])

a='bucaramanga'
b='medellin'
c='bogota'
d='manizales'
e='boyaca'

v1=a[0:1]

print(v1+b[0:2]) #el 0 es la posicion de inicio  2 l cantidad de caracteres a capturar
"""
"""
a=12
b=15

if a==b:
    print ('son iguales')
else:
    print('no son iguales')

a=12
b='15'

print(a+int(b))

"""

#===============  leer nombre, edad,  peso  =======================
"""
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
peso = input('Ingrese su peso: ')
print('Su nombre es:\t '+nombre+'\nSu edad es:\t '+edad+'\nSu peso es:\t '+peso)
"""

#============  convertir letras a min, may  primera a may  =============#
"""
nombre=input('Ingese su nombre completo: ')
print(nombre.lower()) #min
print(nombre.upper())
print(nombre.title())
"""


#pedir 3 notas y promediar
"""
num1 = float(input('Digite un nota 1: '))
num2 = float(input('Digite un nota 2: '))
num3 = float(input('Digite un nota 3: '))

res = (num1+num2+num3)/3
print(res)
"""


#===========  CONDICIONAL IF ==============#

# num1 = float(input('Digite un nota 1: '))
# num2 = float(input('Digite un nota 2: '))
# num3 = float(input('Digite un nota 3: '))
# res = (num1+num2+num3)/3
# print(num1)
# type(num1)

# if num1<0 and num1>5:

#     #if res > 3:
#     #    print('Usted fue aprobado, su nota es: ',round(res,2))


#     if num1<5 and num1>0 or num2<5 and num2>0 or num3<5 and num3>0  :
#         if res>3:
#             print('Usted fue aprobado, su nota es: '+res)
#         else:
#             print('Usted ha reprobado, su nota es: '+round(res,2))
# else:
#     print('Los datos ingresados son erroneos, el numero debe ser mayor a 0 y menor a 5')


# print(round(res,2))



#================== API's request =====================

import requests
import json

#url = "https://restcountries.eu/rest/v2/all"
'''
url = "https://restcountries.eu/rest/v2/lang/en"#paises por idioma
response = requests.request("GET",url)
lista = json.loads(response.text)
'''

#print(response.text)
#print(json.dumps(lista, indent=4)) #indent idena el codigo en 4 espacios

#for pais in lista:
#  print(pais['name'])
'''
url = "https://restcountries.eu/rest/v2/lang/es?fields=name;capital"#paises por idioma
response = requests.request("GET",url)
lista = json.loads(response.text)

for pais in lista:
  print(pais['name']+' = '+pais['capital'])
'''

#=============================================================================

import requests
import json

# url = 'https://api.spotify.com/v1/browse/new-releases'
# token = 'Bearer BQBpZ2Qv4cT_hfKYrVvkW7r582W90PSVO3sSfnC7Jh4CeYBzKkbgVQ0EUKlincXjQNlMt2WAXVg6wlYPpuc'
# # response = requests.request('GET',url)
# # print(response.text)
# head = {
#     'Authorization' : token
# }

# response = requests.request('GET',url, headers = head)

# lista = json.loads(response.text)
# print(json.dumps(lista, indent=4))

# url = "https://api.spotify.com/v1/search?q={}&type={}&limit={}".format("metallica","artist","1")
# token = 'Bearer BQBpZ2Qv4cT_hfKYrVvkW7r582W90PSVO3sSfnC7Jh4CeYBzKkbgVQ0EUKlincXjQNlMt2WAXVg6wlYPpuc'
# # response = requests.request('GET',url)
# # print(response.text)
# head = {
#     'Authorization' : token
# }

# response = requests.request('GET',url, headers = head)

# lista = json.loads(response.text)
# print(json.dumps(lista, indent=4))



# url = "https://api.spotify.com/v1/artists/{}/albums".format("2ye2Wgw4gimLv2eAKyk1NB")# response = requests.request('GET',url)
# # print(response.text)
# head = {
#     'Authorization' 
# }

# response = requests.request('GET',url, headers = head)

# lista = json.loads(response.text)
# print(json.dumps(lista, indent=4))


#============ WHILE MENU ==================
# import random
# import sys

# cont = 0

# while cont == 0:
#     print('\n\n********** MENU ************\n')
#     print('1. Suma')
#     print('2. Resta')
#     print('3. Multiplicacion')
#     print('4. Division')
#     print('5. Mostrar matriz')
#     print('6. Salir')   

#     try:
#         opcion = int(input('\nIngrese una opcion: '))
#         if opcion > 0 and opcion <= 6:

#             if opcion == 1:
#                 num1 = int(input('\nDigite el primer valor: '))
#                 num2 = int(input('Digite el segundo valor: '))
#                 suma = num1+num2
#                 print('La suma es = ',str(suma))

#                 seleccion = input('\nDesea continuar s/n: ')
#                 if seleccion == 's':
#                     cont = 0
#                 else:
#                     cont = 1

#             if opcion == 2:
#                 num1 = int(input('\nDigite el primer valor: '))
#                 num2 = int(input('Digite el segundo valor: '))
#                 resta = num1-num2
#                 print('La resta es = ',str(resta))
#                 seleccion = input('\nDesea continuar s/n: ')
#                 if seleccion == 's':
#                     cont = 0
#                 else:
#                     cont = 1

#             if opcion == 3:
#                 num1 = float(input('\nDigite el primer valor: '))
#                 num2 = float(input('Digite el segundo valor: '))
#                 mult = num1*num2
#                 print('La multiplicacion es = ',str(round(mult,2)))
#                 seleccion = input('\nDesea continuar s/n: ')
#                 if seleccion == 's':
#                     cont = 0
#                 else:
#                     cont = 1


#             if opcion == 4:
#                 x = 0
#                 while x == 0:
#                     try:
#                         num1 = float(input('\nDigite el primer valor: '))
#                         num2 = float(input('Digite el segundo valor: '))
#                         divi = num1/num2
#                         print('La division es = ',str(round(divi,2)))
#                         x = 1
#                         seleccion = input('\nDesea continuar s/n: ')
#                         if seleccion == 's':
#                             cont = 0
#                         else:
#                             cont = 1
#                     except ZeroDivisionError:
#                         print('Error: ',sys.exc_info()[0])
#                         print('\nError, no se puede dividir por cero.\nIngrese los valores de nuevo\n')                       
                    
                
#             if opcion == 5:
#                 fil = int(input('\nDigite la cantidad de filas = '))
#                 col = int(input('Digite la cantidad de columnas = '))
#                 print('\n')

#                 for i in range(0,fil):
#                     for i in range(1,col):
#                         print(random.randint(0,50),end='\t')
#                     print(random.randint(0,50))
#                 seleccion = input('\nDesea continuar s/n: ')
#                 if seleccion == 's':
#                     cont = 0
#                 else:
#                     cont = 1
#             if opcion == 6:
#                 cont = 2
#         else:
#             print('Opcion incorrecta!')    

         
#     except:
#         print('\nDebe ingresar solo numeros\nIntentelo de nuevo...')
        
        

#======================== LISTAS ========================
#import sys


# nombres = ['nicole','jose','esteban','daniela','antonella','nicolas','felipe','david','juliana',
# True,False,123,569,'estella',563,'felipe','daniela','lorena','daniela','\n']
# apellidos = ['torres','perez','rodriguez','fernandez','martinez','malagon',str(123),'mendieta',str(True),'parrado','roldan',str(True),str(False),str(123),str(563),'\n']
# print('\nCantidad de datos en el Array = ',len(nombres))
# nombres.append('mariana')
# espacios=' - '
# print(espacios.join(apellidos))
# cont = 0
# nombres[4] = 'liliana'
# print(nombres)
# print('\nExiste ',nombres.count('daniela'),' veces\n')
# print ('\nEl dto inresado se encuentra en la posicion ',nombres.index('daniela'))
# print('\nElimina el ultimo numero de la lista',nombres.pop(),'\n')#elimina el utlimo numero de la lista
# print('Elimina el primer valor que se le pasa al metodo',nombres.remove('daniela'))
# print('Invierte el orden de la lista ',nombres.reverse())
# print('El metodo sort ordena en forma ascendente los datos de la lista',nombres.sort())
# oracion = 'El metodo split sirve para separar las palabras en una oracion'
# print('El metodo split sirve para separar las palabras en una oracion',oracion.split())
# for n in nombres:
#     cont = cont+1
#     print(n,apellidos[cont])

# # .join() with lists
# numeros = ['1', '2', '3', '4']
# espacios = ' - '
# print(espacios.join(numeros))
    
    
#========================= INTERFACES ===========================

# import tkinter

# def operacion():
#     print('ejecucion exitosa')

# def obtenerDatos():
#     datos = txtEntrada.get()
#     print(datos)
#     titulo['text'] = datos

# ventana = tkinter.Tk() 
# ventana.geometry('500x400') 
# ventana.title('Ventana prueba')
# ventana.resizable(0,0) #primer valor width, heith se puede usar tambien true and alse
# #ventana.iconbitmap('/ruta')
# ventana.config(bg='#de3c2f') #color de form
# titulo = tkinter.Label(ventana, text = 'Python Form', bg='grey')
# txtEntrada = tkinter.Entry(ventana)
# btnSalir = tkinter.Button(ventana, text = 'Salir', command = obtenerDatos)
# titulo.pack(fill = tkinter.X)
# txtEntrada.pack()
# btnSalir.pack(side='right', anchor='s') 
# btnSalir.config(cursor='hand2')

# ventana.mainloop()

#===========================================================

# import tkinter

# ventana = tkinter.Tk()
# ventana.title('Formulario')
# ventana.geometry('500x400')

# lblNombre = tkinter.Label(ventana, text='Nicolas es un fasti', 
# fg='red', font=(14))#.place(x=100, y=200)
# lblNombre.place(x=200, y=100)
# #imagen = tkinter.PhotoImage(file='/ruta.extension')
# #lblNombre = tkinter.Label(ventana, imagen=imagen)
# # txtDatos = tkinter.Entry(ventana).place(x=30, y=20)
# txtDatos = tkinter.Entry(ventana)
# txtDatos.grid(row=2, column=2)

# ventana.mainloop()

#======================================================

# from tkinter import Tk, Label
# # rw = row | cl = column
# raiz = Tk()
# for rw in range(4):
#     for cl in range(8):
#         Label(raiz, text=' (Row %s) \n (Column = %s) ' % (rw, cl),
#               borderwidth=15).grid(row=rw, column=cl)
# raiz.mainloop()

#========================================================

# from tkinter import *

# ventana = Tk()

# frame = Frame(ventana, width=700, height=500)
# frame.pack()

# txtNombre = Entry(frame)
# txtNombre.grid(row=0, column=1, padx=10, pady=10)
# txtNombre.config(fg='#de3c2f', justify='center')
# txtApellido = Entry(frame)
# txtApellido.grid(row=1, column=1, padx=10, pady=10)
# txtPass = Entry(frame)
# txtPass.grid(row=2, column=1, padx=10, pady=10)
# txtPass.config(show='*')
# txtDireccion = Entry(frame)
# txtDireccion.grid(row=3, column=1, padx=10, pady=10)
# txtTelefono = Entry(frame)
# txtTelefono.grid(row=4, column=1, padx=10, pady=10)
# #================ SCROLLBAR =====================
# txtMensaje = Text(frame, width=23, height=5)
# txtMensaje.grid(row=5, column=1, padx=10, pady=10)
# scroll = Scrollbar(frame, command=txtMensaje.yview)
# scroll.grid(row=5, column=2, sticky='nsew')
# txtMensaje.config(yscrollcommand=scroll.set)

# lblNombre = Label(frame, text='Nombre: ')
# lblNombre.grid(row=0, column=0, sticky='e', padx=10, pady=10)
# lblApellido = Label(frame, text='Apellido: ')
# lblApellido.grid(row=1, column=0, sticky='e', padx=10, pady=10)
# lblPass = Label(frame, text='PassWord: ')
# lblPass.grid(row=2, column=0, sticky='e', padx=10, pady=10)
# lblDireccion = Label(frame, text='Direccion: ')
# lblDireccion.grid(row=3, column=0, sticky='e', padx=10, pady=10)
# lblTelefono = Label(frame, text='Telefono: ')
# lblTelefono.grid(row=4, column=0, sticky='e', padx=10, pady=10)
# lblMensaje = Label(frame, text='Telefono: ')
# lblMensaje.grid(row=5, column=0, sticky='e', padx=10, pady=10)
# btnEnviar = Button(frame, text='Ingresar')
# btnEnviar.grid(row=6, column=1, padx=10, pady=10, sticky='e')

# #funcion sticky = sout=s, north=n, east=e, west=w   

# ventana.mainloop()

#==================== CALCULADORA =====================
# from tkinter import*

# principal = Tk()
# ventana = Frame(principal)
# ventana.pack()

# #==================== VARIABLES =======================
# operaciones = ''
# res = 0
# op = ''

# #==================== FUNCIONES =======================

# def teclaPresionada(num):
#     global operaciones
#     global op
#     if operaciones!='':
#         if operaciones=='suma':
#             numeroaMostrar.set(num)
#             operaciones = ''
#             op = 'suma'
#         elif operaciones=='resta':
#             numeroaMostrar.set(num)
#             operaciones=''
#         elif operaciones=='multiplicacion':
#             print(num)
#             numeroaMostrar.set(num)
#             operaciones=''
#         elif operaciones=='division':
#             numeroaMostrar.set(num)
#     else:    
#         numeroaMostrar.set(numeroaMostrar.get()+num)

# def suma(num):
#     global operaciones
#     global res

#     print('res1 = ',res)
#     res+=int(num)
#     print('res2 = ',res)
#     operaciones = 'suma'

#     numeroaMostrar.set(res)

# def resta(num):
#     global operaciones
#     global res

#     res-=int(num)
#     operaciones = 'resta'

# def multiplicacion(num):
#     global operaciones
#     global res   
#     res2 = 
       

#     print('el numero capturado es =',num)
#     print('res1 = ',res)
#     res=int(num)
#     res2*=res
#     print('res2 = ',res,'\nres3 = ',res2)
#     print(type(res))
#     operaciones = 'multiplicacion'
#     numeroaMostrar.set(res)

# def division(num):
#     global operaciones
#     global res

#     res/=int(num)
#     operaciones = 'dividir'

# def igual():
#     global res
#     global op

#     print(op)

#     if op=='suma':
#         numeroaMostrar.set(res+int(numeroaMostrar.get()))
#         res = 0
#         op = ''





# #==================== pantalla ========================
# numeroaMostrar = StringVar()

# display = Entry(ventana, textvariable=numeroaMostrar)
# display.grid(row=1, column=0, padx=10, pady=15, colistalumnspan=4, sticky='nsew')
# display.config(bg='gray', fg='#03f943', justify='right')





# #============== primera fila botones div ==================

# boton7 = Button(ventana, width=3, text='7', command=lambda:teclaPresionada('7'))
# boton7.grid(row=2, column=1)
# boton8 = Button(ventana, width=3, text='8', command=lambda:teclaPresionada('8'))
# boton8.grid(row=2, column=2)
# boton9 = Button(ventana, width=3, text='9', command=lambda:teclaPresionada('9'))
# boton9.grid(row=2, column=3)
# botonDiv = Button(ventana, width=3, text='/')
# botonDiv.grid(row=2, column=4)

# #============== segunda fila botones multi ==================

# boton6 = Button(ventana, width=3, text='6', command=lambda:teclaPresionada('6'))
# boton6.grid(row=3, column=1)
# boton5 = Button(ventana, width=3, text='5', command=lambda:teclaPresionada('5'))
# boton5.grid(row=3, column=2)
# boton4 = Button(ventana, width=3, text='4', command=lambda:teclaPresionada('4'))
# boton4.grid(row=3, column=3)
# botonMult = Button(ventana, width=3, text='X', command=lambda:multiplicacion(numeroaMostrar.get()))
# botonMult.grid(row=3, column=4)

# #============== tercera fila botones resta ==================

# boton3 = Button(ventana, width=3, text='3', command=lambda:teclaPresionada('3'))
# boton3.grid(row=4, column=1)
# boton2 = Button(ventana, width=3, text='2', command=lambda:teclaPresionada('2'))
# boton2.grid(row=4, column=2)
# boton1 = Button(ventana, width=3, text='1', command=lambda:teclaPresionada('1'))
# boton1.grid(row=4, column=3)
# botonRest = Button(ventana, width=3, text='-', command=lambda:resta(numeroaMostrar.get()))
# botonRest.grid(row=4, column=4)

# #============== tercera fila botones suma ==================

# botonPunto = Button(ventana, width=3, text='.')
# botonPunto.grid(row=5, column=1)
# boton0 = Button(ventana, width=3, text='0', command=lambda:teclaPresionada('0'))
# boton0.grid(row=5, column=2)
# botonIgual = Button(ventana, width=3, text='=', command=lambda:igual())
# botonIgual.grid(row=5, column=3)
# botonSuma = Button(ventana, width=3, text='+', command=lambda:suma(numeroaMostrar.get()))
# botonSuma.grid(row=5, column=4)



# principal.mainloop()

#================= END CALCULADORA ==================


#================= LISTAS APP ======================
#from operaciones import sumaLista

# def sumaLista(list): 
#     print('hola')
#     suma=0
#     for n in lista:
#         print(n)
#         suma+=n
#         print('La suma = ',suma)
#     return suma
    
# lista=[]

# num = int(input('Ingrese un numero: '))
# while num!=0:
#     lista.append(num)
#     num = int(input('Ingrese un numero: '))
    
# lista.sort()
# print(lista)

# print('El resultado es = ',sumaLista(lista))


#=================== FUNCIONES ==================
#from operaciones import *

# letras = []
# dato = input("Digite una letra: ")
# for i in letras:
#     if i not in letras:
#         letras.append(i)
# print(letras)


#==================== MENU FUNCIONES =======================
'''
opcion = 0

while opcion!='6': 

    print('\n*********** MENU ***********')
    print('*                          *')
    print('*     1. Suma              *')
    print('*     2. Resta             *')
    print('*     3. Multiplicacion    *')
    print('*     4. Division          *')
    print('*     5. Mostrar Array     *')
    print('*     6. Salir             *')
    print('*                          *')
    print('****************************')

    opcion = input('\nSeleccione una opcion: ')
    # num1 = float(input('\nDigite el primer valor: '))
    # num2 = float(input('Digite el segundo valor: '))     
     
    if opcion == '1' or opcion == 'suma':
        try:
            num1 = float(input('\nDigite el primer valor: '))
            num2 = float(input('Digite el segundo valor: '))  
            print('\n******************************************')       
            print('El resultado de la suma es = ',suma(num1, num2))
            print('******************************************\n') 
            opcion = input('* Para continuar presione cualquier tecla.\n* Para salir digite 6 :')
            
        except:
            print("Debe ingresar unicamente valores numericos.")

            

    elif opcion == '2' or opcion == 'resta':
        try:
            num1 = float(input('\nDigite el primer valor: '))
            num2 = float(input('Digite el segundo valor: '))  
            print('\n******************************************')       
            print('El resultado de la resta es = ',resta(num1, num2))
            print('******************************************\n') 
            opcion = input('* Para continuar presione cualquier tecla.\n* Para salir digite 6 :')

        except:
            print("Debe ingresar unicamente valores numericos.")
        
    elif opcion == '3' or opcion == 'multiplicacion':
        try:
            num1 = float(input('\nDigite el primer valor: '))
            num2 = float(input('Digite el segundo valor: '))    
            print('\n******************************************')       
            print('El resultado de la multiplicacion es = ',multi(num1, num2))
            print('******************************************\n') 
            opcion = input('* Para continuar presione cualquier tecla.\n* Para salir digite 6 :')

        except:
            print("Debe ingresar unicamente valores numericos.")
       
    elif opcion == '4' or opcion == 'division':
        try:
            num1 = float(input('\nDigite el primer valor: '))
            num2 = float(input('Digite el segundo valor: '))  
            print('\n******************************************')       
            print('El resultado de la division es = ',div(num1, num2))
            print('******************************************\n') 
            opcion = input('* Para continuar presione cualquier tecla.\n* Para salir digite 6 :')
        
        except ZeroDivisionError:          
            print("ERROR!!!  No se puede dividir por cero")
            print('******************************************\n')
          
        except:
            print("Debe ingresar unicamente valores numericos.")
        
    elif opcion == '5':
        lista=[]
        llenarLista(lista)

        print('\n******************************************')       
        print('Los datos en la lista son...\n',lista)
        print('******************************************\n') 
        opcion = input('* Para continuar presione cualquier tecla.\n* Para salir digite 6 :')
    elif opcion == '6':
        print('\n******************************************')       
        print('Desea finalizar el proceso?\nLa apliacion sera cerrada.\n')
        print('******************************************') 
        opcion = input('* Para continuar presione cualquier tecla.\n* Para salir digite 6 :')
    else:
        print('\n******************************************')       
        print('La opcion seleccionada no es valida!!!\n')
        print('******************************************') 
        opcion = input('* Para continuar presione cualquier tecla.\n* Para salir digite 6 :')


#=================== FIN MENU FUNCIONES ==================
'''

#=================== LISTAS EN LISTAS ====================
import random

'''
l1 = []
l1 = ([5,6,9,8,4,2])
print(l1)

print('===================')

l2 = []
for i in range(2):
    l2.append([])
    for j in range(3):
        l2[i].append(0)

print(l2)
'''

#================== ejer menu 2 =====================
'''
from operaciones import menu




salir = True
nombres = []

menu()

while salir == True:

    try:
        menu()
        opcion = int(input('\nSeleccione una opcion: '))

        if opcion > 0 and opcion <= 8:

            if opcion == 1:
                nombres.append((entrarNombre(), entrarNota()))
                #print(ingresarNombre(nombres))

            elif opcion == 2:
                buscarEstudiante(nombres)
            elif opcion == 3:
                modificarNota()
            elif opcion == 4:
                listarEstudianteNombre()
            elif opcion == 5:
                listarEstudianteNota()
            elif opcion == 6:
                notaPromedio()
            elif opcion == 7:
                borrarEstudiante()



                if opcion == 1:
                    print('lo encontro')

        else:
            print('Opcion no valida')

        if opcion == 8:
            salir = False

    except:
        print('Ingrese una opcion valida')



'''
#=================== FIN LISTAS EN LISTAS ================
        
    
#===================== DICCIONARIOS =======================
'''
idiomas={'colombia':'español','españa':'español','alemania':'aleman','francia':'frances, italiano'}

print(idiomas)
print(idiomas['francia'])
print(len(idiomas))
print(idiomas.keys())
print(idiomas.values())
print(idiomas.get('francia'))
#del idiomas['colombia']
#print(idiomas)
idiomas['francia']='espanol','aleman','frances' #asignar nuevo valor
print(idiomas)
'''
#===================== END DICCIONARIOS =======================

#===================== METODO BURBUJA =========================
'''
def leerLista():
    lista=[]
    cant = int(input('Ingrese la cantidad de datos a ingresar: '))
    for i in range(cant):
        lista.append(int(input(f"Digite el valor No.{i+1}: ")))
    return lista

def burbuja(lista, tam):
    for i in range(1,tam):
        for j in range(0,tam-1):
            if lista[j]>lista[i]:
                k = lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=k


def imprimirLista(lista):
    for i in range(len(lista)):
        print(lista[i])


a = leerLista()
print(a)
burbuja(a,len(a))
imprimirLista(a)
print(a)
'''
#===================== METODO BURBUJA =========================

#===================== METODO SHELL =========================
'''
def leerLista():
    lista=[]
    cant = int(input('Ingrese la cantidad de datos a ingresar: '))
    for i in range(cant):
        lista.append(int(input(f"Digite el valor No.'{i+1}': ")))
    return lista

def shell(lista, tam):
    i = 1
    for i in range(1,tam,i*3+1):
        while i>0:
            for x in range(i,tam):
                j=x
                tmp=lista[x]
                while j>=i and lista[j-i]>tmp:
                    lista[j]=lista[j-i]
                    j-j-i
                lista[j]=tmp
            i=float(i/2)




def imprimirLista(lista):
    for i in range(len(lista)):
        print(lista[i])


a = leerLista()
print(a)
shell(a,len(a))
imprimirLista(a)
print(a)
'''
#===================== END METODO SHELL =========================

#===================== METODO QUICKSORT =========================
'''
def leerLista():
    lista=[]
    cant = int(input('Ingrese la cantidad de datos a ingresar: '))
    for i in range(cant):
        lista.append(int(input(f"Digite el valor No.{i+1}: ")))
    return lista


def quicksort(lista,izq,der):
    i=izq
    j=der
    x=lista[(izq+der)//2]
    while i<=j:
        while lista[i]<x and j<=der:
            i=i+1
        while x<lista[j] and j>izq:
            j=j-1
        if i<=j:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
            i=i+1
            j=j+1
        if izq<j:
            quicksort(lista,izq,j)
        if i<der:
            quicksort(lista,i,der)


def imprimirLista(lista):
    for i in range(len(lista)):
        print(lista[i])


a = leerLista()
print(a)
quicksort(a,0,len(a)-1)
imprimirLista(a)
print(a)
'''
#===================== END METODO QUICKSORT =========================
    

#===================== METODO DIRECTO =========================
'''
def leerLista():
    lista=[]
    cant = int(input('Ingrese la cantidad de datos a ingresar: '))
    for i in range(cant):
        lista.append(int(input(f"Digite el valor No.{i+1}: ")))
    return lista

def insercionDirecta(lista, tam):
    for i in range(1,tam):
        v=lista[i]
        j=i-1
        while j>=0 and lista[j]>v:
            lista[j+1]=lista[j]
            j=j-1
        lista[j+1]=v



def imprimirLista(lista,tam):
    for i in range(tam):
        print(lista[i])


a = leerLista()
print(a)
insercionDirecta(a,len(a))
imprimirLista(a,len(a))
print(a)
'''
#===================== END METODO DIRECTO =========================

#===================== METODO INSERCION BINARIA =========================
'''
def leerLista():
    lista=[]
    cant = int(input('Ingrese la cantidad de datos a ingresar: '))
    for i in range(cant):
        lista.append(int(input(f"Digite el valor No.{i+1}: ")))
    return lista

def insercionBinaria(lista, tam):
    for i in range(1,tam):
        aux=lista[i]
        izq=0
        der=i-1
        while izq<=der:
            m=(izq+der)//2
            if aux<lista[m]:
                der=m-1
            else:
                izq=m+1
            j=j-1
            while j>=izq:
                lista[j+1]=lista[j]
                j=j-1
            lista[izq]=aux




def imprimirLista(lista,tam):
    for i in range(tam):
        print(lista[i])


a = leerLista()
print(a)
insercionBinaria(a,len(a))
imprimirLista(a,len(a))
print(a)
'''
#===================== METODO INSERCION BINARIA =========================


#===================== METODO SELECCION =========================
'''
def leerLista():
    lista=[]
    cant = int(input('Ingrese la cantidad de datos a ingresar: '))
    for i in range(cant):
        lista.append(int(input(f"Digite el valor No.{i+1}: ")))
    return lista
'''
'''
def seleccion(lista, tam):
    for i in range(0,tam-1):
        min=i
        for j in range(i+1,tam):
            if lista[min]>lista[j]:
                min=j
        aux=lista[min]
        lista[min]=lista[i]
        lista[i]=aux
'''
'''
def seleccion1(lista):
    for i in range(len(lista)-1):
        menor=i
        for j in range(i+1,len(lista)):
            if lista[menor]>lista[j]:
                menor=j
            tmp=lista[menor]
            lista[menor]=lista[i]
            lista[i]=tmp

def imprimirLista1(lista):
    for i in range(len(lista)):
        print(lista[i])


x = leerLista()
print(x)
seleccion1(x)
imprimirLista1(x)
print(x)


def imprimirLista(lista,tam):
    for i in range(tam):
        print(lista[i])
'''

'''
a = leerLista()
print(a)
seleccion(a,len(a))
imprimirLista(a,len(a))
print(a)
'''
#===================== END METODO SELECCION =========================

#===================== END METODO HEAPSORT =========================
'''
def leerLista():
    lista=[]
    cant = int(input('Ingrese la cantidad de datos a ingresar: '))
    for i in range(cant):
        lista.append(int(input(f"Digite el valor No.{i+1}: ")))
    return lista


def heapsort(lista):
    for i in range(len(lista)-1,-1,-1):
        for i in range(0,i):
            item=lista[i]
            j=int((i+1)/2)
            while j>=0 and lista[j]<item:
                lista[i]=lista[j]
                i=j
                j=int(j/2)
            lista[i]=item
        tmp=lista[0]
    lista[0]=lista[i]
    lista[i]=tmp


def imprimirLista1(lista):
    for i in range(len(lista)):
        print(lista[i])


x = leerLista()
print(x)
seleccion1(x)
leerLista()
'''
#===================== END METODO SELECCION =========================

#===================== METODO BUSQUEDA SECUENCIAL =========================
'''
def busquedaLineal(lista, x):
    i=0
    for z in lista:
        if z==x:
            return i
        i+=1
    return f'El numero {x} no existe'


lista=[5,9,12,56,78]
x = int(input('Digite un numero: '))
print(busquedaLineal(lista,x))
'''
#===================== END METODO BUSQUEDA SECUENCIAL =========================

#===================== METODO BUSQUEDA BINARIA =========================

'''
def busquedaBinaria(unaLista, item):
	    if len(unaLista) == 0:
	        return False
	    else:
	        puntoMedio = len(unaLista)//2
	        if unaLista[puntoMedio]==item:
	          return True
	        else:
	          if item<unaLista[puntoMedio]:
	            return busquedaBinaria(unaLista[:puntoMedio],item)
	          else:
	            return busquedaBinaria(unaLista[puntoMedio+1:],item)

listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

print(busquedaBinaria(listaPrueba, 3))
print(busquedaBinaria(listaPrueba, 13))


def busquedaBinaria(unaLista, item):
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = False

    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)//2
        if unaLista[puntoMedio] == item:
            encontrado = True
        else:
            if item < unaLista[puntoMedio]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado

listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(busquedaBinaria(listaPrueba, 3))
print(busquedaBinaria(listaPrueba, 13))
'''
#-------------------------------
'''
def busquedaBinaria(lista, x):
    izq=0
    der=len(lista)
    while izq<=der:
        medio=(izq+der)//2
        print('izq: ',izq,'der',der,'medio',medio)
        if lista[medio]==x:
            return medio
        elif lista[medio]>x:
            der=medio-1
        else:
            izq=medio+1
    return -1

def leerLista():
    lista=[]
    cant=int(input('Digite la cantidad de nuemros a ingresar: '))
    for i in range(cant):
        lista.append(int(input(f'Ingrese No.{i} ')))
    return lista

a=leerLista()
print(a)
x=int(input('Numero a buscar = '))
r = resultado=busquedaBinaria(a,x)
print(f'El resultado esta en la posicion {r}')
#-----------------------------------
'''


#===================== END METODO BUSQUEDA BINARIA =========================

#===================== RECURSIVIDAD =========================
from math import factorial
'''
#--------sin libreria--------
def factorialRecursiva(n):
    return 1 if n==0 else n*factorialRecursiva(n-1)

a=factorialRecursiva(5)
print(f'el factorial de forma recursiva es {a}')

#--------con libreria------------
b=factorial(5)
print(f'el factorial con libreria es {b}')

#-------con while----------------
def fac(n):
    res=1
    while n>1:
        res*=n
        n-=1
    return res


c=fac(5)
print(f'el factorial con libreria es {c}')

'''
'''
#================fibonacci====================
def fibonacci(x):
    return 0 if x == 0 else 1 if x==1 else fibonacci(x-1)+fibonacci(x-2)

f=fibonacci(10)
print(f'fibonacci {f}')

#--------------iterativo----------------
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

f1=fibo(10)
print(f'fibonacci iterativo {f}')
#================end fibonacci====================
'''
'''
#----------------listar recursividad--------------
def cabeza(lista):
    return lista[0]

def cola(lista):
    return lista[1:]

def maximo(lista):
    if (len(lista)==1):
        return cabeza(lista)

    head=cabeza(lista)
    maximacola=maximo(cola(lista))
    return head if head>maximacola else maximacola

def sumalista(lista):
    if(len(lista)==0):
        return 0
    return cabeza(lista)+sumalista(cola(lista))

def reducir(lista,funcion):
    if len(lista)==1:
        return lista[0]
    return funcion(cabeza(lista), reducir(cola(lista),funcion))


a=maximo([1,3,5,7,9])
print(f'el valor maximo de la lista es {a}')
b=sumalista([5,8,12,9,15])
print(f'la suma de la lista es {b}')
c=reducir([5,9,8,1,7],lambda x,y:x+y)
print(f'la reduccion de la lista es {c}')

'''
#===================== END RECURSIVIDAD =========================


#===================== LECTURA DE ARCHIVOS =========================
'''
ruta='/home/nian/Documentos/minTIC/python/reto2/hola.txt'
contenido='jose,pepe,juan'
archivo=open(ruta,'w')
'''


#===================== END LECTURA DE ARCHIVOS =========================

import json
'''
with open('data.json') as file:
    data-json.load(file)

    for cliente in data['clientes']:
        print('nombre: ',cliente['nombre'])
        print('apellido: ',cliente['apellido'])
        print('edad: ',cliente['edad'])
        print('ciudad: ',cliente['ciudad'])

'''

#url = "https://restcountries.eu/rest/v2/lang/en"#paises por idioma
#url = 'url = "https://restcountries.eu/rest/v2/lang/es?fields=name;capital"'
url = "https://www.datos.gov.co/api/views/gt2j-8ykr/rows.json?fields=name"
response = requests.request("GET",url)
lista = json.loads(response.text)
print(lista)



