import csv

field = ['Name', 'ID', 'Price', 'Categories', 'Stock']

Products = []
IDList = []
PriceList = []
Categories = []
StockList = []
for i in range(1, 5):
    Products.append("Mile" + '' + str(i))
    IDList.append(i)
    PriceList.append("15")
    Categories.append("MILES")
    StockList.append("1")
filename = "Products.csv"

rows = zip(Products, IDList, PriceList, Categories, StockList)
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)

