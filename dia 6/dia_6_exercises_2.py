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
# Exercises: Level 2

#7 Unpack siblings and parents from family_members
s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,*papás=family_members
print(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
print(papás)
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits= ('banana apple orange watermelon mango'.split() )
vegetables=('carrot onion tomato potato'.split())
animal=('milk cheese meat cream bacon eggs'.split())
food_stuff_tp=fruits + vegetables + animal
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
number=((len(food_stuff_lt)))
half=number/2
print(food_stuff_lt[0:int(half)] , (food_stuff_lt[int(half)+1:number]))

#Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[3:(number)-3])
#Delete the food_staff_tp tuple completely
del food_stuff_tp
#Check if an item exists in tuple:
'no sale nada marca error'

#Check if 'Estonia' is a nordic country3
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)

#REVISADO
print("Revisado")