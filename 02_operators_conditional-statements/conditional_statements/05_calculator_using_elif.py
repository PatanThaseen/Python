n1=float(input("Enter a number:"))
n2=float(input("Enter a number:"))
print("For Addition:+\nFor Subtraction=-\nFor multiplication:*\nFor division:/\nFor module:%")
operator=input()
if(operator=='+'):
    print("Addition is:",n1+n2)
elif(operator=='-'):
    print("Subtraction is:",n1-n2)
elif(operator=='*'):
    print("Multiplication is:",n1*n2)
elif(operator=='/'):
    if(n2==0):
        print("Division by zero is not allowed")
    else:    
        print("Division is:",n1/n2)
elif(operator=='%'):
    print("Module is",n1%n2)
else:
    print("select valid operator") 