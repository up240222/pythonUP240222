#Exercises: Level 2
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
n=0
for i in range (101):
    n += i
    print(n)
#The sum of all numbers is 5050.



    
#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sumapar=0
sumaimpar=0
for i in range(101):
    if i % 2 ==0:
        sumapar+=i
    else:
        sumaimpar+=i
print('la suma par  es de ', sumapar)
print('la suma impar  es de ', sumaimpar)


#The sum of all evens is 2550. And the sum of all odds is 2500.