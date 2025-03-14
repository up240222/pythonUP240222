
#Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ageset = set(age)
print ('len age is : ', len(age))
print('len ageset is : ', len(ageset))
if len(age) > len(ageset):
    print('el mas largo es :' , len(age) )
else:
   print('el mas largo es :' , len(ageset) ) 

#2 Explain the difference between the following data types: string, list, tuple and set
'''the type string is the type of a sentence, it detects it like words, the list is a serie of data in brackets that could be modified and the tupple is in parenthesis but
can not be modified, a set can be modified but can not repeat items
'''
#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
n='I am a teacher and I love to inspire and teach people'
sentence = ('I am a teacher and I love to inspire and teach people'.split())
set_sentence= set(sentence)
print('ahi hay ', len(set_sentence), 'unicas palabras en la oración: ', n)



#REVISADO
print("Revisado")