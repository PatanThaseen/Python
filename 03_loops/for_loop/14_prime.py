import math
a=int(input("Enter Start value:"))
b=int(input("Enter end value:"))
print(f"The prime numbers between {a} and {b} are:")
for i in range(a,b+1):
    if i<=1:
        print("Not a prime number")
    else:
        is_prime=(math.factorial(i-1)+1)%i==0
    if is_prime:
        print(i,end=" ")