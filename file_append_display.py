with open('for_test.txt', 'a') as file:
    file.write('\nso its little bit hard to learn the python concepts')
    file.close()
    display = open('for_test.txt')
    print(display.read())