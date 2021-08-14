#Open the csv file given in pdf and download it in form of  .CSV
#Open the data file outside the folder ,you will see in form of excel
#Issue in file 13 columns but only 11 headers
#Go to the main page ..all exoplanets data are given which contains the list of expoplanets tha
# #If you click on the list of expoplanets it will take you to the individual planets link
#You will the individual data ,The eccentricity header is misplaced,The last two columns have no header
#Orbital radius header is misplaced..#So we have to give temporary headers_sent
#Since discovery date and mass is appearing twice in the CSV file 
# so that's why will add a temporary discovery date and temporary_mass header
#You need to open the HTML page link given in the document and there you have to open PSComp link to show the entire data to the student but again go back to the solution of GitHub link
# From there download data set_2.CSV in the folder 
#The goal is to arrange planets in alphabetical order


#This file is for sorting and arranging the planets in alphabetical order and then we will merge the fsorted data with downl


import csv

data = [] #empty list

with open("dataset_2.csv", "r") as f:   #reading the csv file
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]  #Here we are storing header
planet_data = data[1:]  #All the data stored here

#Converting all planet names to lower case
for data_point in planet_data:
    data_point[2] = data_point[2].lower() #Third Column ,pl_name is converted into lower case

#Sorting planet names in alphabetical order
#In Python, a lambda function is a single-line function declared with no name, which can have any number of arguments, but it can only have one expression. 
# Such a function is capable of behaving similarly to a regular function declared using the Python's def keyword.
#The sorted() function returns a sorted list of the specified iterable object. 

#Here we are sorting the planet_data that is planet name in our order using sorting function .
# then we are storing in planet_data

planet_data.sort(key=lambda planet_data: planet_data[2])

#We are storing the data in another csv file
with open("dataset_2_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)