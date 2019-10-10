""" get the list of records that are sold in year 2017"""

import csv

opn = open('100_sales_record.csv')
reed = csv.reader(opn)
lis = list(reed)
print(lis[0])
for year in lis:
    year[7].split('/')
    if '2017' in year[7]:
        print(year)
