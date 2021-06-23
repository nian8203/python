num = int(input('\nIngrese la tabla que desea ver: '))
res = 0
for i in range(10):
    tabla = num*(i+1)
    print(str(num)+' X '+str(i+1)+' = '+str(tabla))