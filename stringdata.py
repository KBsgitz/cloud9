# python 3.8

# put a string in a variable, print the string, the data type and convert and combine into a final string
myString = "This a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# further string combinations
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# string inputs
name = input("What is your name? ")
print(name)

color = input("What is your favourite color? ")
animal = input("What is your favourite animal? ")

# print with multiple variables using curly braces and .format
print("{}, you like a {} {}!".format(name,color,animal))
