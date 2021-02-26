# 計算各毛色數量

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
print(df)