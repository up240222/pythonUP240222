#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
print ( 'Thirty' + ' days' + ' of' ' python')

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print ( 'Coding' + ' for' + ' all')

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding for all"

#4  Print the variable company using _print()_.
print ( company )

#5 Print the length of the company string 
len_company=len (company)
print ( len_company)

#6 Change all the characters to uppercase letters using _upper()_ method.
print (company.upper())

# 7 Change all the characters to lowercase letters using _lower()_ method.
print(company.lower )

#8 Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print (company.capitalize())
print (company.title())
print (company.swapcase())

#9 Cut(slice) out the first word of _Coding For All_ string.
print ( company[0:6])

#10 Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print (company.find ("Coding"))
print (company.index ("Coding"))

# 11  Replace the word coding in the string 'Coding For All' to Python.
print (company.replace ("Coding" , "Python"))

#12 Change Python for Everyone to Python for All using the replace method or other methods.
comp = "Python for Everyone"
print (comp.replace ("Everyone" , "All"))

#13 Split the string 'Coding For All' using space as the separator (split()) .
print (company.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print ("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

#15 What is the character at index 0 in the string _Coding For All_.
print(company[0])

#16 What is the last index of the string _Coding For All_
print (company[-1])

#17 What character is at index 10 in "Coding For All" string.
print (company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'
acronym = comp[0] + comp[7] + comp[-8] 
print( acronym)

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
acr= company[0] + company[-7] + company [-3]
print(acr)

#20 Use index to determine the position of the first occurrence of C in Coding For All.
print (company.index  ('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
print ( company.index ('f'))

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.}
print (company.rfind ('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
ucannot = 'You cannot end a sentence with because because because is a conjuntion'
print (ucannot.find ('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print (ucannot.rindex ('because'))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print ( ucannot[31:-16])

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word = 'because'
print (ucannot.index(word))

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print ( ucannot[31:-16])

#28 Does '\'Coding For All' start with a substring _Coding_?
print (company.startswith('Coding'))

#29 Does 'Coding For All' end with a substring _coding_?
print (company.endswith ('coding'))

#30 '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
remove ='Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'
print (remove.strip (' &nbsp; '))

#31 Which one of the following variables return True when we use the method isidentifier():
    #- 30DaysOfPython
    #- thirty_days_of_python
print ('30DaysOfPython'.isidentifier())
print ('thirty_days_of_python'.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
pylibrary= [' ' , 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' #'.join(pylibrary)
print (result)

#33 Use the new line escape sequence to separate the following sentences.
# ```py
 #   I am enjoying this challenge.
   # I just wonder what is next.
  #  ```
print('I am enjoying this challenge.\nI just wonder what is next')

#34 Use a tab escape sequence to write the following lines.
 #   ```py
  #  Name      Age     Country   City
   #     Asabeneh  250     Finland   Helsinki
print ('\tName      \tAge  \tCountry \tCity ')
print( '\tAsabeneh  \t250  \tFinland \tHelsinki ')

#35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with radius %d is %.2f. meters square.' %(radius, area)
print ( formated_string)    

#36 Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
a = 8
b =6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) 
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
