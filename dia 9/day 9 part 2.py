### Exercises: Level 2

#1. Write a code which gives grade to students according to theirs scores:
'''sh
        80-100, A
        70-89, B
        60-69, C
        50-59, D
        0-49, F
        '''
puntuation=int(input('put your puntuation '))
if 80<=puntuation and puntuation<=100:
    print('Your grade is A')
elif 70<=puntuation and puntuation<=89:
    print('Your grade is B')
elif 60<=puntuation and puntuation<=69:
    print('Your grade is C')
elif 50<=puntuation and puntuation<=59:
    print('Your grade is D')
else:
    print('Your grade is F')

#1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
    '''September, October or November, the season is Autumn.
    December, January or February, the season is Winter.
    March, April or May, the season is Spring
    June, July or August, the season is Summer'''
month=str(input('put the month '))
if month=='September' or month=='October' or month=='November':
    print ('The season is Autumn')
elif month=='December' or month=='January' or month=='February':
    print('the season is winter')
elif month=='March' or month=='April' or month=='May':
    print('the season is spring' )
else:
    print('the season is summer')

 #2. The following list contains some fruits: la tengo mal al rato la cambio

    '''sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=(str(input('add a fruit to the list ')))
if fruit in fruits:
    print('That fruit already exist in the list')
    print(fruits)
else:
    fruits.append(fruit)
    print(fruits)