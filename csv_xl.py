"""get the list of records that are item type clothes"""


import csv
opn = open('100_sales_record.csv')
red = csv.reader(opn)
rows = list(red)
print(rows[0])
for column in rows:
    if 'Clothes' in column:

        print(column)

