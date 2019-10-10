from itertools import islice
with open('for_test.txt', 'r') as x:
    sli = islice(x, 1)
    for how in sli:
        print(how)
