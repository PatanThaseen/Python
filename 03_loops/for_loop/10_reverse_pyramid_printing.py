n=int(input("Enter n value:"))
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(2*(n-i)-1):
        print("*",end=" ")
    print()

