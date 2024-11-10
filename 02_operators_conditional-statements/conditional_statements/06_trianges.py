side1=int(input("Enter a side value:"))
side2=int(input("Enter a side value:"))
side3=int(input("Enter a side value:"))
if(side1+side2>side3 and side2+side3>side1 and side3+side1>side2):

    if(side1==side2==side3):
        print("The triangle is equilateral")
    elif(side1==side2 or side2==side3 or side3==side1):
        print("The triangle is isosceles")
    else:
        print("The triangle is scalar")
else:
    print("The entered sides donot form a valid triangle")        