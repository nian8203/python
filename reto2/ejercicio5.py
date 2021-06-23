num = 0
pasw = '123456'
cont = 0

while cont<1:
    
    num = input('\nIngrese su contraseña: ')
    print
    if num == pasw:
        cont=cont+1
        print('\nContraseña correcta\nBienvenido!\n')
    else:
        print('\nLa contraseña ingresada es erronea\nIntentelo de nuevo')

   