#LEVEL2
#1 Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def uppercase (country):
    return country.upper()
result=map(uppercase, countries)
print(list(result))

#2 Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square_num (num):
    return num**2
result=map(square_num, numbers)
print(list(result))

#3 Use map to change each name to uppercase in the names list
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def uppercase_name(name):
    return name.upper()
resul=map(uppercase_name, names)
print(list(resul))

#4 Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def lan_country (country):
    if 'land' in country:
        return True
    return False
result= filter(lan_country, countries)
print(list(result))

#5 Use filter to filter out countries having exactly six characters.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def six_ch_country(ch):
    if len(ch)==6:
        return True
    return False
result=filter(six_ch_country,countries )
print(list(result))

#6  Use filter to filter out countries containing six letters and more in the country list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def six_ch_or_more_country(pais):
    if len(pais)>=6:
        return True
    return False
result=filter(six_ch_or_more_country, countries)
print(list(result))

#7 Use filter to filter out countries starting with an 'E'
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def countries_w_e(pais):
    return pais.startswith('E')
result=(filter(countries_w_e,countries ))
print(list(result))

#8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from functools import reduce
resultado=( lambda x, y: x + y,map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(resultado)

#9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
lista = [1,2,3,'LETRAS','Paulo','palabras']
def get_string_list(list):
    return[cosa for cosa in lista if isinstance(cosa, str)]
resultado=get_string_list(lista)
print(resultado)

#10 Use reduce to sum all the numbers in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def add_num (x,y):
    return int(x) + int(y)
suma=reduce(add_num, numbers)
print(suma)

#11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def pais_sentence(x,y):
    return x + ', ' + y 
oracion=reduce(pais_sentence,countries )
oracion1= oracion+'los paises son de Europa '
print(oracion1)

#12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries_lista import countries 

def categorize_countries(countries , pattern):
    return list(filter(lambda pais: pattern in pais.lower(),countries))
print(categorize_countries(countries,'land'))

#13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_initial(countries ):
    return dict(map(lambda letter: (letter, sum(1 for country in countries if country.startswith(letter))), sorted(set(map(lambda x: x[0], countries)))))
print(count_countries_initial(countries))

#14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten():
    ten= [p for p in countries[:10]]
    return ten
print(get_first_ten())

#15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten():
    ten= [p for p in countries[-10:]]
    return ten
print(get_last_ten())

print("Revisado")