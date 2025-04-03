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
print(evens_and_odds())
            
