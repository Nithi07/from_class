b_year = int(input())
can_hei = input('').split(' ')
a = []
for i in can_hei[:b_year]:
    if i not in a:
        a.append(int(i))
print(a.count(max(a)))
