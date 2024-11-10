amount=int(input("Enter the amount you need to withdraw:"))
balance=100000
if(amount<balance):
    balance=balance-amount
    print("Your withdrawl is successful!")
    print("Balance after your withdrawl is:",balance)
else:
    print("insufficient balance")    