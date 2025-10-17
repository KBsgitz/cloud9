# python 3.8

# defining a list with multiple data types

myMixedTypeList = [45, 290578, 1.02, True, "My cat is on the bed.", "45"]
# 'for' loop to go through each item, state what it is and the date type
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
