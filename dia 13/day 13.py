#EXERCISES DAY 13
#1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero=[i for i in numbers if i<=0]
print(negative_and_zero)

#Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

#output [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista=[number for linea in list_of_lists for number in linea]
lista_aplastada=[number for linea in lista for number in linea]
print(lista_aplastada)

#3 Using list comprehension create the following list of tuples:

'''[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]'''

result = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
for item in result:
    print(item)

#4Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
paises=[country for line in countries for country in line]
print(paises)
result = [[name.upper(), name[:3].upper(), capital.upper()] for (name, capital) in paises]
print(result)

#5 Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
'''[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]'''

result = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]

#6 Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
result = [' '.join(name_tuple) for [(name_tuple)] in names]
print(result)

#7 Write a lambda function which can solve a slope or y-intercept of linear functions.
linear_solver = lambda x1, y1, x2, y2, solve_for: (
    (y2 - y1) / (x2 - x1) #formula de la ´pendiente
    if solve_for == 'slope' 
    else         
    y1 - ((y2 - y1) / (x2 - x1)) * x1 
    if solve_for == 'y-intercept' else None)
m = linear_solver(2, 4, 6, 8, 'slope')       
b = linear_solver(2, 4, 6, 8, 'y-intercept')   

print(f"La ecuación de la recta es: y = {m}x + {b}")
print("Revisado")