import csv

data = [
    ["Name", "Age", "Location"],
    ["Jhon", "25", "New York"],
    ["Jane", "30", "Los Angeles"]
]

path = "output.csv"

# #寫入
# with open(path, "w", newline="") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)
# #讀取
# with open(path, "r") as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)

with open("output1.csv", "a", encoding="utf-8-sig")as file:
    file.write("姓名, 年齡 , 地點")
    file.write("\n迪龍, 22, 台灣")