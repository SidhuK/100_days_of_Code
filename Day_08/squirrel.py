import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(f"Number of gray squirrels is {gray_squirrels_count} ")
print(f"Number of black squirrels is {black_squirrels_count} ")
print(f"Number of red squirrels is {red_squirrels_count} ")

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")