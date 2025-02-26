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

#10 .Compare the slopes in tasks 8 and 9.
if m == pendiente:
    print ("las pendientes son iguales")
elif m>pendiente:    
    print ("la primera pendiente es mayor")
else:
    print ("la segunda pendiente es mayor")

#11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

a= 1
b = 6
c = 9
x =( -b +-((b * b ) - 4*(a * c))**.5)/2 * a
print (x)
print ("coloque el valor de x" , x )
y = (  x*x + 6*x + 9)
print ("el valor de y es : " ,y)

#12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print ("largo de pyhton y de dragon " )
len_pyhton=len('python')
len_dragon=len('dragon')
falsy_comp=len_pyhton == len_dragon
print (" lenght of python is :",{ len_pyhton})
print (" lenght of python is :",{ len_dragon})
print ("falsy comparission ( length of python  == length of dragon ) : ,", falsy_comp )

#13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
on_both = 'on' in 'python' and 'on' in 'dragon'
if on_both == True :
    print ("the word 'on' is found in both words")
else :
    print ("la palabra no se encuentra en las palabras")

#14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print ( "check if the word jargon is in the sentence")
sentence =' I hope this course is not full of jargon'
jargon_sentence = 'jargon' in sentence
if jargon_sentence == True :
    print ("the word 'jargon is found in the sentence " )
else :
    print ("the word is not found in the sentence")

#15 There is no 'on' in both dragon and python
on_both = 'on' in 'python' and 'on' in 'dragon'
if on_both == True :
    print ("the word 'on' is not found in the sentence")
else :
    print ("the word is found in the sentence")

#16 Find the length of the text python and convert the value to float and convert it to string
print ("largo de pyhton " )
len_pyhton=len('python')
print ( " el largo de la palabra es : " , len_pyhton )
len_pyhton=float(len_pyhton)
print( " se convirtió el valor " , type (len_pyhton))
len_pyhton=str(len_pyhton)
print( " se convirtió el valor " , type (len_pyhton))

#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

num=( int(input("put a number")))
par= num % 2 == 0
if par ==True:
    print ("el número es par " )
else :
    print ( " el número es impar")

##18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
division = 7/3
d = float (7/3)
equal = d == division
print("the number is equal: ", equal)

##19. Check if type of '10' is equal to type of 10
typ = int('10')
t=(10)
c=typ==t
print("type'10' is equal to 10: ",c)

##20.Check if int('9.8') is equal to 10
ch = float('9.8')
c= int(ch)
d=10
compare=c==d
print("int('9.8') es igual a 10: ",compare)

##21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours=int(input("ingresa las horas que trabajaste: "))
pay=float(input("cuanto te pagan por hora: "))
r=hours*pay
print("your pay is about :", r)

##22.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years =int(input(" "))
seconds= years  * 365 * 24 * 3600
hundred_years_to_second = 100 * 365 * 24 * 3600
secondsleft= hundred_years_to_second - years
print ( "seconds left are : " , secondsleft)
  
#23 Write a Python script that displays the following table
print("a   a^0   a^ 1 a^2 a^3")
for a in range (1 , 6):
    print(f" {a} {a**0} {a**1} {a**2}  {a**3}")
