#  Declare a function add_two_numbers. It takes two parameters and it returns a sum
def add_two_numbers ():
    num1= float(input('put a number'))
    num2= float(input('put another number'))
    suma= num1 + num2
    return 'la suma es: ', suma
print(add_two_numbers())

#2Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle():
    π=3.1416
    r=float(input('put the radius'))
    area = π * r * r
    return 'el area es', area
print(area_of_circle())

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums():
   numrandom= input('put the the number of your preference')
   if '.' in numrandom:
       numrandom= float(numrandom)
       print('El tipo de numero ', numrandom, ' que ingresaste es:', type(numrandom))
   elif '.' in numrandom == False:
        numrandom = int(numrandom)
        print ('El tipo de numero ', numrandom, ' que ingresaste es:', type(numrandom))
   else:
        print('Error el numero ', numrandom,  'no es valido.')
print(add_all_nums())

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_f():
    c=float(input('put the celsius temperature'))
    F = (((c * 9)/5) + 32)
    return 'la temperatura en farenheit es:', F
print(convert_celsius_to_f())

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season():
    Autumn = {'September', 'Septiembre', 'October', 'Octubre', 'November', 'Noviembre'}
    Winter = {'Dicember', 'Diciembre', 'January', 'Enero', 'February', 'Febrero'}
    Spring = {'March', 'Marzo', 'April', 'Abril', 'May', 'Mayo'}
    Summer = {'June', 'Junio', 'July', 'Julio', 'Agust', 'Agosto'}
    month= str(input('put the month'))
    if month in Autumn:
        print('the season is: Autumn' )
    elif month in Winter:
        print('the season is: Winter' )
    elif month in Spring:
        print('the season is: Spring' )
    elif month in Summer:
        print('the season is: Summer' )
    else:
        print('error en el mes puesto')
print(check_season())

#Write a function called calculate_slope which return the slope of a linear equation
x1=float(input('put the ecuation value x1: ' ))
x2=float(input('put the ecuation value x2: ' ))
y1=float(input('put the ecuation value y1: ' ))
y2=float(input('put the ecuation value y2: ' ))
def calculate_slope(x1, y1, x2, y2):
    slope=((y2-y1)/x2-x1)
    return slope 
print(calculate_slope(x1, y1, x2, y2))

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
a=float(input('put the ecuation value a: ' ))
b=float(input('put the ecuation value b: ' ))
c=float(input('put the ecuation value c: ' ))
def solve_quadratic_eqn(a,b,c):
    variable1=-b +((b*b)-(4*a*c)**.5)/(2*a)
    variable2=-b -((b*b)-(4*a*c)**.5)/(2*a)
    return variable1 and variable2
print(solve_quadratic_eqn(a,b,c))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
def print_list():
    listaa=['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
    return listaa
print(print_list())

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list():
    listaa.reverse()
    return listaa
listaa=['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
print(reverse_list())

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items():
    listaa=['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
mayuscula=[item.upper() for item in listaa]
print(mayuscula)
print(capitalize_list_items)

#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item():
    listaa=['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
    new_item=str(input('put the new item '))
    listaa.append(new_item)
    return listaa
print(add_item())
# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it. 
def remove_item():
     listaa=['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
     remo_item=str(input('put the item you wanna quit'))
     listaa.pop(remo_item)
     return listaa
print(remove_item())

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers():
    r=int(input('put the range'))
    suma=0
    for i in range (r+1):
        suma +=i
    return suma
print(sum_of_numbers())

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds():
    r=int(input('put the range'))
    s=0
    for i in range(1, r+1, 2):
        s+=i
    return (s)

print(sum_of_odds())

#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even():
    r=int(input('put the range'))
    s=0
    for i in range(0, r+1, 2):
        s+=i
    return (s)
print(sum_of_even())

print("Revisado")





