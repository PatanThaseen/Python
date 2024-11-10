n=int(input("Enter a number:"))
temp=n
sum=0
while(temp>0):
    remainder=temp%10
    sum=sum+remainder
    temp//=10

print("The sum of digits of given number is",sum)    