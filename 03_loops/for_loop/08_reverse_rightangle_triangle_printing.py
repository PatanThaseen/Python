n=int(input('Enter n value:'))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ") 
        num=num+1
    print()    