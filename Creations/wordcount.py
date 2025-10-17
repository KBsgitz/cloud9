# python 3.8
# word counter

# request at least a sentence from the user (and put it in a var)
sentence = input("Enter at least a sentence... ")
# split the sentence into separate words/strings and use len to return number of those
wordCount = (len(sentence.split()))
# print the number of those as an integer
print(int(wordCount))


