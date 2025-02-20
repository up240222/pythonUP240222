##EJERCICIOS

##Area del circulo

radio=30
pi=3.1416
areaOfCircle=pi*radio**2
circumOfCircle=2*pi*radio
print( 'El area del circulo es de:', areaOfCircle)
print('La circunferencia del', circumOfCircle)

# radio del circulo

radio=int(input('Inserte el radio del circulo:'))
areaOfCircle=pi*radio*radio
circumOfCircle=2*pi*radio
print( 'El area del circulo es de:', areaOfCircle)
print('La circunferencia del', circumOfCircle)

Nombre=input('Ingrese su nombre:')
Apellido=input('Ingrese sus apellidos:')
País=input('ingrese su país de origen:')
Edad=int(input('Ingrese su edad:'))


print('Tu nombre es: ' + Nombre ,Apellido,
      'Eres de :' + País,
      'Tu edad es de :',Edad)
print(type(Nombre))
print(type(Apellido))
print(type(País))
print(type(Edad))