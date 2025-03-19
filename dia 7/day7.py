#1 Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
#2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Amd', 'Nvidia', 'Samsung'])
print(it_companies)
#4 Remove one of the companies from the set it_companies
it_companies.remove('Amd')
print (it_companies)
#5 What is the difference between remove and discard
print('''The difference is that remove method only works when the item is in the set, but if not the program crash or does not work
      so we use discard because if the item is not found in the list it will comtinue assuming that the item is eliminated or does 
      not exist''')

#REVISADO
print("Revisado")