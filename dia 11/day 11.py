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