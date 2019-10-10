import pandas as pd
opn = pd.read_csv('100_sales_record.csv')
pri = opn['Item Type']
crr = opn['Country']
print(pri, crr)