#LEVEL 1
#1 Explain the difference between map, filter, and reduce

#ej
'''numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16]'''# la funcion de lambda x:x**2 significa que al valor x o sea cada elemnto de la lista se le aplica lo que sigue de dos puntos  y maps es para aplicarlo en cada uno de los elementos y filter es para solo sacar a los que si cumplen la funcion
'''
map es el que aplica una función a cada elemento de una lista 
filter es para solo sacar a los que si cumplen la funcion por eso el nombre de filtrar
Reduce una lista a un solo valor aplicando una función acumulativa. Necesitas importarla desde functools.

'''
#2 Explain the difference between higher order function, closure and decorator
'''
Función de Orden Superior (Higher Order Function)
Es una función que:
-Recibe otra función como argumento, o

-Devuelve una función como resultado. es decir, es una funcion donde le enseñas lo que quieres hacer
ejemplo:
def saludar(nombre):
    return f"Hola, {nombre}"
def procesar_saludo(funcion):
    return funcion("Lucía")

print(procesar_saludo(saludar)) aqui ya le enseñaste que es saludar y solo llamas la funcion con otra funcion

Una closure es una función interna que recuerda las variables del entorno donde fue creada, incluso si ese entorno ya terminó.
Ejemplo:

python
Copiar
Editar
def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

por_dos = crear_multiplicador(2)
print(por_dos(5))  

Un decorador es una función que modifica o extiende el comportamiento de otra función, sin cambiar su código original.

'''
#3Define a call function before map, filter or reduce, see examples
'Significa que antes de hacer el map, filter o reduce, tú defines primero la función con def, y luego la pasas como argumento, en lugar de usar lambda.'
#4 Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print(country)

#5 Use for to print each name in the names list.
names= ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway','Iceland']
for name in names:
    print(name)

#6 Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)

print("Revisado")


