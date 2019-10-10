try:
    message = int(input('age: '))
    print(message)
except:
    print('enter valid data')


try:
    message = int(input('age: '))
    avg = 1000 / message
    print(avg)
except ZeroDivisionError:
    print('invalid number')