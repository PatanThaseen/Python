import math
num=int(input())
if num<=1:
    print("Not a prime num")
else:
    is_prime=(math.factorial(num-1)+1)%num==0
    if is_prime:
        print("Prime Number")
    else:
        print("Not a prime")        