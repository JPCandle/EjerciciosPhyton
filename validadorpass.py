contraseña_inicial = input('Ingrese su contraseña')
contraseña_denuevo = input('Ingrese de nuevo su contraseña para confirmar')

contraseña_exacta = contraseña_inicial == contraseña_denuevo

if len[contraseña_inicial < 8]:
    print('Su contraseña debe ser mayor a 8 digitos') 

else: 
    print('Su contraseña es correcta')