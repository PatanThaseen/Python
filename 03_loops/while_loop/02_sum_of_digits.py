n=int(input("Enter a number:"))
sum=0
while n>0:
    remainder=n%10
    sum=sum+remainder
    n//=10
print(sum)    
 