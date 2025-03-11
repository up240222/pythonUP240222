#Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#1 Join A and B
B.update(A)
print(B)
#2 Find A intersection B
print(B.intersection(A))

#3 Is A subset of B
'subset es cuando engloba lo de un set, es decir, un subset tiene informacion de un set, y un set tine información de un superset'
print(A.issubset(B))
#4 Are A and B disjoint sets
'cuando no tienen en comun se llaman disjoint'
print(A.isdisjoint(B))
#5 Join A with B and B with A
print(A.union(B) )
print((B.union(A)))
#6 What is the symmetric difference between A and B
'dice cuales eran los que no coincidian en ambos sets'
print(A.symmetric_difference(B))
#7 Delete the sets completely
del A
del B
