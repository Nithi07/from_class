""" Find only the total revenue for the following items
Office Supplies, Snacks, Meat, Fruits

and give the result in the following format:
{'office Supplies': total_revenue,
'Snacks': total_revenue,
'Meat': total_revenue,
'Fruits': total_revenue}
"""
import csv

opn = open('100_sales_record.csv')
reed = csv.reader(opn)
lis = list(reed)
dic = {}
for row in lis:
    if 'Office Supplies' in row:
        dic[row[2]] = float(row[11])
    elif 'Fruits' in row:
        dic[row[2]] = float(row[11])
    elif 'Meat' in row:
        dic[row[2]] = float(row[11])
    elif 'Snacks' in row:
        dic[row[2]] = float(row[11])

print(dic)