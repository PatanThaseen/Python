#list
l=[1,2,3,4]
print(tuple(l))
print(str(l))
print(set(l))
print(tuple(l))
#we cannot convert a list directly into a dictionary but it can be done by using "fromkeys" function
l1=[1,2,3,4]
l2=['A']
print(dict.fromkeys(l1,l2))