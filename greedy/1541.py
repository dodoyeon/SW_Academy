# 잃어버린 괄호
elist = list(input())
num = []
op = []
s = ''
for i in range(len(elist)):
    item = elist[i]
    if item == '+' or item == '-':
        num.append(int(s))
        op.append(item)
        s = ''
    else:
        s += item
num.append(int(s))
del elist

n = num[0]
for i in range(len(op)):
    item = op[i]
    if item == '+':
        n += num[i+1]
    elif item == '-':
        n -= sum(num[i+1:])
        break
print(n)