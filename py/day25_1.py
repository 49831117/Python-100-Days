# # 逐行讀取 .csv 檔案
# with open(".py\\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# csv
# import csv
# with open(".py\\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data) 
#     # >>>  <_csv.reader object at 0x000002467C411EE0>
#     # this object can be lopped through
#     for row in data:
#         print(row)


# # 抽取氣溫資訊
# import csv
# with open(".py\\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)



# Pandas
from numpy.lib.function_base import average
import pandas as pd
data = pd.read_csv(".py\\weather_data.csv")
# print(type(data))
# print(list(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
temp_list = data["temp"].to_list()
# print(average(temp_list))  # list 用
# print(data["temp"].mean())  # series 用
# print(max(temp_list)) # list 用
# print(data["temp"].max()) # series 用

# # Get Data in Columns ### 屬性名稱要完全一樣
# print(data["condition"]) # 把 data 當字典
# print(data.condition)  # 把 data 當物件

# # Get Data in Row ########## 印出來不一樣
# print(data[data.day == "Monday"]) # 1 by 3
# print(data[data["day"] == "Monday"]) # 1 by 3，同上
# print(data.iloc[1]) # 3 by 1

# # print the day which has the maimum temperature
# print(data[data.temp == data.temp.max()])
# print(data[data["temp"] == max(data["temp"])])

# monday = data[data.day == "Monday"]
# print(monday["condition"])
# print(monday.condition)

# monday_temp = int(data[data.day == "Monday"].temp)
# print( 32 + monday_temp * 9/5)

# Creat a Dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data = pd.DataFrame(data_dict)
# print(data)
data.to_csv('.py\\test.csv')


