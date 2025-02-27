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


