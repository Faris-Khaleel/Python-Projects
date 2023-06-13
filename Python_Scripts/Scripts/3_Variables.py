# Python has no reserved word for declaring a variable

# Variables

x = 5  # int

print("x = ", end="")
print(x)

x2 = "Faris"  # string

print("x2 = ", end="")
print(x2)

x3 = 3.5  # float

print("x3 = ", end="")
print(x3)


# Casting/changing values to other data types

x4 = str(5)  # cast to string

print("x4 = " + str(x4) + " of type " + str(type(x4).__name__))

x5 = int("5")  # cast to integer (will give error if you put a string)

print("x5 = " + str(x5) + " of type " + str(type(x5).__name__))

x6 = float(5)  # cast to float

print("x6 = " + str(x6) + " of type " + str(type(x6).__name__))


x7, x8, x9 = "Orange", "Banana", "Cherry"  # Assign Multiple Values

x10 = x11 = x12 = "Orange"  # One Value to Multiple Variables
