a=int(input("Enter a num:"))
b=int(input("Enter a num:"))
c=int(input("Enter a num:"))
if(a>b and a>c):
    print(a,"is greater")
elif(b>c):
    print(b,"is greater")
elif(a==b and b==c and c==a):
    print("All numbers are equal")    
else:
    print(c,"is greater")    


