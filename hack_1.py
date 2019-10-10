num = input().split(' ')
a = []
for i in num:
    a.append(int(i))
print((sum(a)-max(a)), (sum(a)-min(a)))