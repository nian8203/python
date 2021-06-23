edad = int(input('\nDigite su edad: '))

if edad > 0:
    if edad < 4:
        print('Su entrada no tiene costo')
    elif edad >= 4 and edad <= 18:
        print('Su entrada tiene un valor de $5000')
    elif edad > 18:
        print('Su entrada tiene un valor de $10000')
else:
    print('La edad ingresada debe ser mayor a 0')
