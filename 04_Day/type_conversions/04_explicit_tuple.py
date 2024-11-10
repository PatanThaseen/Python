#tuple
t=("Thaseen",35,20)
print(list(t))
print(set(t))
print(str(t))
#we cannot convert a tuple directly into a dictionary but it can be done by using "fromkeys" function
t1=(1,2,3,4)
t2=('A')
print(dict.fromkeys(t1,t2))
