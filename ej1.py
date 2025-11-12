
nombre = input("Ingresa tu nombre: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
anio_actual = 2025 
edad = anio_actual - anio_nacimiento

if edad >= 18:
    print("Eres mayor de edad")    
else:
    print("Eres menor de edad")

print(f"Hola {nombre}, tu edad es: {edad} años de edad.")





