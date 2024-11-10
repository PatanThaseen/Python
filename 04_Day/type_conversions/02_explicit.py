#int(value,base)-> Converts a string to an integer based on the specified base (binary, octal, decimal, or hexadecimal).
#The base value can be (2,8,10,16)
#The value inside double quotes should be of corresponding base value
x="101"
y=int(x,2)
# a=int(x,8)
# b=int(x,10)
# c=int(x,16)
print(y)

#float(value or variable)->Converts a value (usually a string) to a floating-point number.
#The value inside double quotes should be of int or float
x="tha"
y=float(x)
print(y,type(y))

#ord()->is used to convert a character to integer
x="a"
y=ord(x)
print(y)

#hex()->is used to convert an integer to hexadecimal(0-15)
x=35
y=hex(x)
print(y)

#oct()->is used to convert an integer to octal(0-7)
x=35
y=oct(x)
print(y)

#list()-> Converts an iterable (like a string, tuple, or set) into a list.
x = "hello"
y = list(x)  # Converts the string to a list of characters
print(y)  # Output: ['h', 'e', 'l', 'l', 'o']

#tuple()-> Converts an iterable (like a string, list, or set) into a tuple.
x = [1, 2, 3]
y = tuple(x)  # Converts the list to a tuple
print(y)  # Output: (1, 2, 3)

#set-> Converts an iterable (like a list, tuple, or string) into a set.
x = [1, 2, 2, 3, 4, 4]
y = set(x)  # Converts the list to a set, removing duplicates
print(y)  # Output: {1, 2, 3, 4}

#dict()->Converts an iterable (usually a list of key-value pairs) into a dictionary.
x = [("name", "Alice"), ("age", 25)]
y = dict(x)  # Converts the list of tuples to a dictionary
print(y)  # Output: {'name': 'Alice', 'age': 25}

# Creating an empty dictionary
z = dict()
print(z)  # Output: {}

#str()->Converts any data type to its string representation.
x = 123
y = str(x)  # Converts integer 123 to the string "123"
print(y)  # Output: "123"

#complex()-> Creates a complex number from real and imaginary parts.
#Usage: complex() can take two arguments, the real part and the imaginary part, or a single string that represents a complex number.
x = complex(3, 4)  # Creates a complex number 3 + 4j
print(x)  # Output: (3+4j)

y = complex("5+2j")  # Creates a complex number from a string
print(y)  # Output: (5+2j)

#chr()-> Converts an integer (Unicode code point) to its corresponding character.
x = 65
y = chr(x)  # Converts the Unicode code point 65 to the character 'A'
print(y)  # Output: 'A'

z = 97
w = chr(z)  # Converts the Unicode code point 97 to the character 'a'
print(w)  # Output: 'a'
