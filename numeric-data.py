#Python 3.8

# Print a string stating three numeric types that Python works with
print("Python has three numberic types: int, float, and complex")
# Create a variable called 'myValue' with the value of 1 (integer) and print it
myValue=1
print(myValue)
# Print the TYPE of variable
print(type(myValue))
# Print a string consisting of my variable, with two separate strings of text
print(str(myValue) + " is of the data type " + str(type(myValue)))

#Repeat steps with a float, complex and booleans
myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
