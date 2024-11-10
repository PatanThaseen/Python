n = int(input("Enter the base value: "))
exponent = int(input("Enter exponent value: "))
result = 1
i = 1

while i <= exponent:
    result *= n
    i += 1

print(result)
