'''
print('hola')
n = []
p = []
num = int(input('Ingrese un numero: '))
while num >= 0:
    n.append(num)
    num = int(input('Ingrese un numero: '))
    if num%2==0:
        p.append(num)

print('La cantidad de numeros ingresados es = '+str(len(n)))
print('Los numeros pares ingresados son = '+str(p))
print('Los numeros ingresados son = '+str(n))
'''
'''
juego = int(input('inrese si o no: '))
if juego == 'the last of us':
    print('seguro que lo quieres: ')
else:
    print('cancelar obcion: ')
'''

juego = input('que juego quieres: ')
if juego == 'the last of us':
    print('seguro que lo quieres: ')
else:
    print('cancelar obcion: ')


