#DAY 5
#1 Declare an empty list
empty_list =list ()

#2Declare a list with more than 5 items
cultures = ['asian' , 'latino' , 'african' , 'indian' , 'russian' ,'american' , 'French']

#3Find the length of your list
print (len(cultures))

#4Get the first item, the middle item and the last item of the list
print ('first item : ', cultures[0]  ,', ', 'middle item : ' , cultures [3] ,' , ''last item : ' , cultures[-1])

#5Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ('Paulo, 18, 1.66, single, Aguascalientes'.split(','))

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ('Facebook , Google , Microsoft, Apple , IBM, Oracle , Amazon'.split(','))
#7 Print the list using print()
print (it_companies)

#8Print the number of companies in the list
print(len(it_companies))

#9Print the first, middle and last company
first_company =(it_companies[0])
middle_company= (it_companies[3])
last_company =(it_companies[-1])
print ('''
    first company of the list  {}
    middle company of the list {}
    last company of the list {}
       '''.format(first_company , middle_company , last_company))

#10Print the list after modifying one of the companies
del it_companies[4]
print (it_companies)

#11Add an IT company to it_companies


#12Insert an IT company in the middle of the companies list

#13Change one of the it_companies names to uppercase (IBM excluded!)

#14Join the it_companies with a string '#;  '

#15Check if a certain company exists in the it_companies list.

#16 Sort the list using sort() method

#17Reverse the list in descending order using reverse() method

#18 Slice out the first 3 companies from the list

#19 Slice out the last 3 companies from the list

#20 Slice out the middle IT company or companies from the list

#21 Remove the first IT company from the list

#22 Remove the middle IT company or companies from the list

#23 Remove the last IT company from the list

#24 Remove all IT companies from the list

#25 Destroy the IT companies list