n=int(input("Enter n value::"))
for i in range(1,n+1):
    if(i%2!=0):
       print(i)

#(or)
n=int(input("Enter n value::"))
for i in range(1,n+1,2):
    print(i)    