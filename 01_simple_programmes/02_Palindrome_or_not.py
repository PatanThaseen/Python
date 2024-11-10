#A palindrome number is a number that reads the same forward and backward:
s=int(input("Enter a number:"))
sum=0
temp=s
while(temp>0):
  remainder=temp%10
  sum=sum*10+remainder
  temp//=10
if(s==sum):
    print("number is Palindrome")   
else:
    print("number is not a Palindrome")   
#for strings
s=input("Enter a string:")
reversed_s=s[::-1]
if(reversed_s==s):
    print("Palindrome")   
else:
    print("Not a Palindrome")  
    
#for strings without using slicing
str=input("Enter a string:")
str=str.replace(" ","").lower()
left=0
right=len(str)-1 
is_palindrome=True
while left<right:
    if str[left]!=str[right]:
      is_palindrome=False
      break
    left+=1
    right-=1
if is_palindrome:
  print("Palindrome") 
else:   
  print("Not a Palindrome")    
    
   
     


