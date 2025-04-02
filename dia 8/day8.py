#1 Create an empty dictionary called dog
dog={}

#2 Add name, color, breed, legs, age to the dog dictionary
dog={
'name':'Max',
'color':'golden',
'breed':'yorki',
'legs': 4,
'age':  3}
print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={'first_name':'Paulo', 
'last_name':'Delgadillo', 
'gender':'masculine', 
'age':18, 
'is married':False, 
'skills':['good_english, fast_learning, well_driving, kind, respectful '], 
'country':'México', 
'city':'Aguascalientes',
'address':{'coto':'Residencial Santa Fe',
           'calle':'5ta cerrada interior 9'}
           }
print(student)
#4 Get the length of the student dictionary
print(len(student))
#5 Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
#6 Modify the skills values by adding one or two skills
student['skills'].append ('Python')
print(student['skills'])
#7 Get the dictionary keys as a list
print(list(student.keys()))

#8 Get the dictionary values as a list
print(list(student.values()))
#9 Change the dictionary to a list of tuples using items() method
print(tuple(student.items()))
#10 Delete one of the items in the dictionary
del (student['skills'])
print(student)
#11 Delete one of the dictionaries
del dog
print("revisado")