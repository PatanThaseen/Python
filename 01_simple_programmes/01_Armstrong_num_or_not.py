#sum of the powers of the digit should be equal to the number itself
n=int(input("Enter a number:"))
length=len(str(n))
sum=0
temp=n
while(n>0):
  remainder=n%10
  sum=sum+pow(remainder,length)
  n//=10
if(sum==temp):
    print("number is armstrong")   
else:
    print("number is not armstrong")  
    
    