import csv

dataset_1 = []
dataset_2 = []

with open("dataset_1.csv", "r") as f:  # The main page ,Pick from github link
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("dataset_2_sorted.csv", "r") as f:  #alphabetically sorted csv files
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0] # headers of dataset 1 stored here
planet_data_1 = dataset_1[1:] ## entire data of dataset 1 stored here

headers_2 = dataset_2[0] # headers of dataset 2 stored here
planet_data_2 = dataset_2[1:] # entire data of dataset 2 stored here

headers = headers_1 + headers_2
planet_data = []

#The enumerate() function allows you to loop over an iterable object and keep track of how many iterations have occurred. 
# Enumerate is particularly useful if you have an array of values that you want to run through entirely.

for index, data_row in enumerate(planet_data_1):   
    planet_data.append(planet_data_1[index] + planet_data_2[index])

#a+ Opens a file for both appending and reading. The file opens in the append mode. 
# If the file does not exist, it creates a new file for reading and writing.
with open("final2.csv", "a+") as f:    
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
