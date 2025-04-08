#LEVEL 3
#1 Write a function called is_prime, which checks if a number is prime.
def is_prime():
    number=int(input('put a number, this will check if your number is prime'))
    if number<=1:
        return ('the number is not prime')
    for i in range(2, int(number ** 0.5) + 1):#los numeros primos no tienen raiz entera
        if number % i == 0:  #dividimos el numero por el rago de valor de i, o sea los valores de i que empieza desde 2 o el otro divisor que es el entero de la raiz cuadrdad y si el residuo es 0 de alguno de esos dos significa que no es primo pero si, el residuo no da 0 en alguno de esos dos divisores es primo 
            return ('the number is not prime')
    return ('the number is  prime', number)
print(is_prime())

#2Write a functions which checks if all items are unique in the list.

def all_unique(lst):
    return len(lst)==len(set(lst))
print('all the numbers in the list are unique?:',all_unique([1,2,2,2,3,4,5,2,4,5,3,6,7,3,7,2,4,5,3,2,2,4,3,4,4,3,3,2,6,7,8]))

#3Write a function which checks if all the items of the list are of the same data type.
def check_data_type(lst):
    return 'la lista es del mismo tipo?: ', len(lst)==0 or all (type (x) ==type(lst[0]) for x in lst ),#para ver si la lista esta vacia, y si no que todos sean igual al primero y el for checa cada uno para ver si son del mismo tipo

print(check_data_type([1,2,2,2,3,'4',5,2,4,5,3,6,7,3,7,2,4,5,3,2,2,4,3,4,4,3,3,2,6,7,8]))

#4Write a function which check if provided variable is a valid python variable
import keyword
def variable_valid (name):
    if keyword.iskeyword(name):#Usamos el modulo keyword para verificar si el nombre es una palabra clave de Python (como for, if, while, etc.).
        print('the name already in predefined names')
    else:
        print(name)
    return 
print(variable_valid('for'))

#5 Go to the data folder and access the countries-data.py file.
#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
#Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
#mayor a menor
from paisdata import paises
def the_most_spoken_languages():
    countrylanguage = []
    for pais in paises:
        for language in pais['languages']:
            countrylanguage.append (language )
            ordenatedlanguage=set(countrylanguage)
    dictionary_languages= {

    }
    for language in ordenatedlanguage:
        dictionary_languages[language]=0
    for idiom in dictionary_languages:
        for pais in paises:
            if idiom in pais['languages']:
                dictionary_languages[idiom]=pais['population'] + dictionary_languages[idiom]
                sortedthingspopulation = sorted(dictionary_languages.values(), reverse=True)
                sorfkeyslanguagespopulation = sorted(dictionary_languages, key= dictionary_languages.get, reverse=True)
    for i in range(0,21):
        
        print(i+1, sorfkeyslanguagespopulation[i] , sortedthingspopulation[i])
    return
print(the_most_spoken_languages())

from paisdata import paises

def the_most_populous_countries():
    country_population = {}
    for pais in paises:
        country_population[pais['name']] = pais['population']
    sorted_population = sorted(country_population.items(), key=lambda item: item[1], reverse=True)#queremos ordenar la population NO EL PAIS, lamda es una funcio compacta como def 
    for i in range(0,20):
        print(i+1,  sorted_population[i])
    return
    
the_most_populous_countries()
print("Revisado")



