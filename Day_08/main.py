# with open("weather_data.csv") as data_file:
#    data = data_file.readiness()
#    print(data)

# using csv module to import a csv file

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)  # makes an object for the data
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# using pandas to do the same thing

import pandas
data = pandas.read_csv("weather_data.csv")  # this is a dataframe
print(data["temp"])  # this is a series

# convert that data into a dictionary
data_dict = data.to_dict()
print(data_dict)

# mean and max temperatures

print(data["temp"].mean())
print(data["temp"].max())
