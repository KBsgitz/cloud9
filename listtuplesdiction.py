# Python 3.8

# Lists are defined with []


myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# accessing the list and printing the result of each (chronological)
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

# changing value of the second object in the list (lists are mutable)
myFruitList[2] = "orange"
print(myFruitList)

# tuples are defined with () which are immutable

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# dictionaries are defined with {} and are mutable, like lists

myFavouriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}

print(myFavouriteFruitDictionary)
print(type(myFavouriteFruitDictionary))

# using the key to recall the value
print(myFavouriteFruitDictionary["Akua"])
print(myFavouriteFruitDictionary["Saanvi"])
print(myFavouriteFruitDictionary["Paulo"])