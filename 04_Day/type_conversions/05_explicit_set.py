s={1,2,3,"T"}
print(tuple(s))
print(str(s))
print(list(s))
#we cannot convert a list directly into a dictionary but it can be done by using "fromkeys" function
s1={1,2,3,4}
s2={'A'}
print(dict.fromkeys(s1,s2))