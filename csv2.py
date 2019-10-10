"""get the list of records that are sold in Sub-Saharan Africa"""

import csv

opn = open('100_sales_record.csv')
red = csv.reader(opn)
lis = list(red)
print(lis[0])
for sold in lis:
    if 'Sub-Saharan Africa' in sold:
        print(sold)


