
for i in range(3):
    edad = int(input('\nIngrese su edad: '))
    ingresos = int(input('Digite sus ingresos mensuales: '))

    if edad > 18 and ingresos > 2000000:
        print('Usted debe tributar')
    else:
        print('Usted no debe tributar')