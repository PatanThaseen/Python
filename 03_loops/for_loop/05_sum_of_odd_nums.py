n=int(input("Enter n value::"))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
      sum=sum+i
print(sum)