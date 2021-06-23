tablas = []
num = int(input('Digite un numero: '))

for i in range(10):
    op = num*(i+1)
    res = num,'X',(i+1),'=',op
    tablas.append(res)
print(tablas)
