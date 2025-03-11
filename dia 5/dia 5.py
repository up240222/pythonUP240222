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
it_companies.append('Intel')
print (it_companies)

#12Insert an IT company in the middle of the companies list
it_companies.insert(3, 'AMD')
print(it_companies)
#13Change one of the it_companies names to uppercase (IBM excluded!)
del it_companies [0]
it_companies.insert  (0 , 'FACEBOOK' )
print (it_companies)
#14Join the it_companies with a string '#;  '
it_companies.append ('#;')
print (it_companies)  
#15Check if a certain company exists in the it_companies list.
check = 'Intel' in it_companies
print ('La siguiente empresa esta en la lista ? :' , check)
#16 Sort the list using sort() method
print (sorted(it_companies))
#17Reverse the list in descending order using reverse() method
print (sorted(it_companies , reverse=True ))
#18 Slice out the first 3 companies from the list
print (it_companies[0:3])
#19 Slice out the last 3 companies from the list
print (it_companies[-4:-1])
#20 Slice out the middle IT company or companies from the list
mid = int(len(it_companies)/2)
print ('la empresa de en medio es ', it_companies[mid])
#21 Remove the first IT company from the list
primeraempresa= str ( it_companies [0])
it_companies.remove (primeraempresa)
print (it_companies)
#22 Remove the middle IT company or companies from the list
it_companies.remove (str(it_companies[mid]))
print (it_companies)
#23 Remove the last IT company from the list
it_companies.remove (str(it_companies[-2]))
print (it_companies)
#24 Remove all IT companies from the list
it_companies.clear()
print (it_companies)
#25 Destroy the IT companies list
del it_companies
#26 Join the following lists:

#  ```py
  #  front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
   # back_end = ['Node','Express', 'MongoDB']
    #```
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
integers = front_end + back_end
print (integers)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = integers
(full_stack.index('Redux'))
full_stack.insert (5 , 'Python')
full_stack.insert (6 ,  'SQL')
print(full_stack)

#exercises level 2
#1. The following is a list of 10 students ages:

#```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages_in_order = (sorted(ages))

print ('the min age is :' , ages_in_order[0] , 'the max age is :', ages_in_order[-1])
(ages_in_order.insert (0 ,ages_in_order[0]) , ages_in_order.insert ( -1 , ages_in_order[-1]) )

print(ages_in_order)
midddle=((len(ages_in_order)//2))

print('the median item is : ' ,ages_in_order[midddle])
average = (sum (ages_in_order))//len(ages_in_order)
print ('the average age is :' , average )

range = max (ages_in_order)-min(ages_in_order)
print (range)
value1=(min(ages_in_order))-(average )
value2 =(max(ages_in_order))-(average)
print (abs(value1 -value2))


