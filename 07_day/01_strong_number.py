# a number where the sum of the factorials of its digits is equal to the number itself:
num=int(input("Enter the number:"))
sum_of_factorials=0
temp=num
while num>0:
    digit=num%10
    factorial=1
    for i in range(1,digit+1):
        factorial=factorial*i
    sum_of_factorials+=factorial
    num=num//10
if sum_of_factorials==temp:
    print("Strong number")       
else:
    print("Not a strong number")