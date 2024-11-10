n=int(input("Enter a number:"))
reverse=0
while n>0:
    r=n%10
    reverse=reverse*10+r
    n//=10
print("The reverse of number is",reverse)    

