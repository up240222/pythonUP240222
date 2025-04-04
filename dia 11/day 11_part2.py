#Exercises: Level 2
#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.cuenta numero de pares o impares a partir de un numero dado
def evens_and_odds():
    x=[]
    y=[]
    number=int(input('put a number'))
    for i in range(number+1):
        if i%2==0:
            x.append(i)
        else:
            y.append(i)
    print(f'los numeros pares son: {x} y los numeros impares son: {y} ')
    print(f'el numer de numeros impares es: {len(y)}, el numero de numeros pares son{len(x)}')
print(evens_and_odds())

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factoriall(n):
    if n==0 or n==1:
        return 1
    else:
        return  n*factoriall(n-1)#esta formula de factorial es lo mismo que poner n!
print(factoriall(5))#poner el valor ahi

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
n= input('put the paramter')
def is_empty():
    if n =='':
        print('the parameter is empty' )
    else:
        print('the parameter is not empty, it cointans:', n )
print(is_empty())

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
numbers=[1,2,2,2,3,4,5,2,4,5,3,6,7,3,7,2,4,5,3,2,2,4,3,4,4,3,3,2,6,7,8]
sorted_numbers=sorted(numbers)
import statistics
def calculate_mean():
    prom=(sum(sorted_numbers))//len(sorted_numbers)
    return prom
def calculate_median():
    numero_mediana=int(len(sorted_numbers))//2
    mediana=sorted_numbers[numero_mediana]
    return mediana
def calculate_mode ():
    moda=statistics.mode(numbers)
    return moda
def calculate_range ():
    valor_min=min(sorted_numbers)
    valor_max=max(sorted_numbers)
    rango=valor_max-valor_min
    return rango
 
def calculate_desviacion_estandar():
    suma=0
    prom=(sum(sorted_numbers))//len(sorted_numbers)
    for valor in numbers:
        suma+=(valor-prom)**2
        radicar= suma / len(sorted_numbers)
        raiz= radicar**.5
    return raiz
def calculate_variance ():
    suma=0
    prom=(sum(sorted_numbers))//len(sorted_numbers)
    for valor in numbers:
        suma+=(valor-prom)**2
        radicar= suma / len(sorted_numbers)
    return radicar
print('la media es:', calculate_mean())
print('la mediana es: ', calculate_median())
print('la moda es :',calculate_mode())
print('el rango es :',calculate_range ())
print('la varianza es:', calculate_variance() )
print('la desviacion estandar es: ',calculate_desviacion_estandar ())






