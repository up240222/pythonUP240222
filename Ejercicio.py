#1. Declare your age as integer variable
age = 18
print(type(age))

#2. Declare your height as a float variable
height = 61
print(type(height))

#3. Declare a variable that store a complex number
complejo = 3+8j
print(type(complejo)) 

#4. Write a script that prompts the user to enter base 
# and height of the triangle and calculate an area of 
# this triangle (area = 0.5 x b x h).
base = float(input("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))
area = 0.5 * base * altura
print("El área del triangulo es de",area,"unidad cuadrada")

#5. Write a script that prompts the user to enter side a, 
# side b, and side c of the triangle. Calculate the perimeter 
# of the triangle (perimeter = a + b + c).
side_a = float(input("Ingresa el valor del primer lado: "))
side_b = float(input("Ingresa el valor del segundo lado: "))
side_c = float(input("Ingresa el valor del tercer lado: "))
perimeter = side_a + side_b + side_c
print("El perimetro del triangulo es de",perimeter,"unidades")

#6. Get length and width of a rectangle using prompt. Calculate 
# its area (area = length x width) and perimeter (perimeter = 2 x (length + width)).
l = float(input("Ingresa el largo del rectangulo: "))
w = float(input("Ingresa el ancho del rectangulo: "))
a = l * w
perimetro = 2*(l + w)
print("El area del rectangulo es de",a,"unidades cuadradas y su perimetro es de",perimetro,"unidades")

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) 
# and circumference (c = 2 x pi x r) where pi = 3.14.
radio = float(input("Ingresa el radio del circulo: "))
pi = 3.14
a = pi * radio * radio
p = 2 * pi *radio
print("El area del circulo es de",a,"unidades cuadradas y su perimetro es de",p,"unidades")

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2.
m = 2
b = -2
x_intercept = -b / m
print("Pendiente (m):",m)
print("Intersección en Y (b):",b)
print("Intersección en X:",x_intercept)

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10).
import math
x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10
pendiente = ((y_2)-(y_1))/((x_2)-(x_1))
euclides = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
print("La pendiente es",pendiente)
print("La distancia de Euclidiana es de",euclides)