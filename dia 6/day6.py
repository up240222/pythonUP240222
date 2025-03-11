#Exercises: Level 1

#1 Create an empty tuple
print (tuple())

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers=('Daniel , Luis, Juan, Carlos '.split())
sisters=('Sofia, Claudia, Gisela, Martha, Lupita'.split())
#3 Join brothers and sisters tuples and assign it to siblings

family= brothers +sisters
print(family)
#4 How many siblings do you have?
print(len(family))
#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
lista =list(family)
lista.append('Pedro' )
lista.append ('Gisela')
family_members =tuple(lista)
print(family_members)
