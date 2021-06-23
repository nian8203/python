perdidas=[]
asignaturas = ['matematicas','español','fisica','quimica','historia','ciencias','ingles','filosoia','etica']

for i in asignaturas:
    print('\n\n================ ',i,' =================')
    nota = input('Ingrese una nota entre 0 y 100 = ')

    if nota < '70':
        perdidas.append(i)

for i in perdidas:
    for j in asignaturas:
        if i==j:
            asignaturas.remove(i)

print('\n\n=============================================================================')
print('aprobadas = ',asignaturas)
print('perdidas = ',perdidas)
print('=============================================================================')

'''

for i in range(len(asignaturas)):

    print('--------- ',asignaturas[i],' ---------\n')
    nota = input('Digite una nota entre 0 y 100 = ')
    print('contador nomral',str(i))

    if nota <= '70':
        perdidas.append(asignaturas[i])
        asignaturas.pop(i)
        print(len(asignaturas)-1)
        print(asignaturas)
        print(perdidas)
        i -=1
        print('cont perdidas = '+str(i))
'''
