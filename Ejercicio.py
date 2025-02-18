#Ejercicio 1 (crear una variable que determina)
#Escribe un script que permita al usuario entregar una base y una altura
#Triangulo y calcular la area y calcular la area de ese triangulo (area = .5 * b * h)
b = float (input ("ingrese la base del triangulo"))
h = float (input ("ingrese la altura del triangulo"))
area = .5 * b * h
print (area)


#Wrte a script that promopts the user to enter the side a, side b, and side c of
# the triangle. calculate the perimeter of the triangle (perimeter = a + b + c)
a = float(input("ingrese el lado a del triangulo"))
b = float(input("ingrese el lado b del triangul"))
c =  float(input("ingrese el lado c del triangulo"))
p = ( a + b + c)
print (p)


#Get lenghtand width of a rectangle using prompt. Calculate its area (area =lenght + width) and
#perimeter (perimeter = 2 x ( length + width)
l = float (input("put the length of the rectangle"))
w = float (input("put the width of the rectangle"))
a = (l + w)
p= (2*(l+w))
print ("el perimetro del rectangulo es :" , p)
print ("el area del rectagulo es de : " , a )

#Get the radious of a circle using prompt. Calculate the area (area = pi * r * r) 
#and the circumference (c= 2 *pi *r) where pi = 3.14
pi = 3.14
r = float (input("put the radious of the circle"))
a = (pi * r * r)
c = ( 2 *pi *r)
print ("the perimeter of the circle is :", p)
print ("the circumference of the circle is : " , c)


#Calculate the slope x-intercept and y-intercept of y= 2x-2
slope = 2
y_intercept=-2
x_intercept = 1
print (f"pendiente(slope) : " , slope)
print (f"intercepto en y (y-intercept) :" , y_intercept)
print (f"intercepto en x (x-intercept) : " , x_intercept )
