# python 3.8

# ’import’ the ability to read the csv file, via the csv module. 
# create a deep copy of the data, via the copy module. 

import csv
import copy

# define dictionary, which will be used as a template of sorts, to then import csv data
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# 'for' loop to establish format to print data in dictionary and hold in following variable
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
    myInventoryList = []
# with open statement will allow the csv file to stay open whilst reading (and closing once that block of code has finished running). 
    with open('car_fleet.csv') as csvFile:
     csvReader = csv.reader(csvFile, delimiter=',')  
     lineCount = 0  
     for row in csvReader:
        if lineCount == 0:
        # this time use of {} to format strings, instead of double quotations
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
    for myCarProperties in myInventoryList:
     for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")