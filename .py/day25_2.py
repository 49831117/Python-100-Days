# 計算各毛色數量
'''
import pandas as pd

data = pd.read_csv(".py\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_g = 0
color_c = 0
color_b = 0

for i in data["Primary Fur Color"]:
    if i == "Gray":
        color_g += 1
    elif i == "Cinnamon":
        color_c += 1
    elif i == "Black":
        color_b += 1

df = pd.DataFrame([["Gray", color_g], ["Cinnamon", color_c], ["Black", color_b]], columns = ["Primary Fur Color", "Count"])
df.to_csv("squirrel_count.csv")


'''
import pandas as pd

data = pd.read_csv(".py\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_g_count = len(data[data["Primary Fur Color"] == "Gray"])
color_c_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
color_b_count = len(data[data["Primary Fur Color"] == "Black"])

df = pd.DataFrame([["Gray", color_g_count], ["Cinnamon", color_c_count], ["Black", color_b_count]], columns = ["Primary Fur Color", "Count"])
df.to_csv(".py\\squirrel_count.csv")


