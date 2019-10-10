def find_maximum():
    message = input('enter numbers: ')
    spl = message.split(",")
    lis = []
    for i in spl:
        lis.append(int(i))
    ma = lis[0]
    for j in lis:
        if j > ma:
            ma = j
    return ma


