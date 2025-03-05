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
#Exercises: Level 2

#Unpack siblings and parents from family_members
s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,*papás=family_members
print(s1,s2,s3,s4,s5,s6,s7,s8,s9,10)
print(papás)
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits= ('banana, apple, orange, watermelon, mango' )
vegetables=('carrot, onion, tomato, potato')
animal=('milk, cheese, meat, cream, bacon, eggs')
food_stuff=fruits + vegetables + animal
print(food_stuff)

#Change the about food_stuff_tp tuple to a food_stuff_lt list

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

#Slice out the first three items and the last three items from food_staff_lt list

#Delete the food_staff_tp tuple completely

#Check if an item exists in tuple:

#Check if 'Estonia' is a nordic country3

#Check if 'Iceland' is a nordic country

#nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')