# n=int(input('Enter n value:'))
# for i in range(n):
#     print(" "*(n-i-1)+"*"*(2*i+1))

n=int(input("Enter n value:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()

