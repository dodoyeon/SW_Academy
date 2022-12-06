#5와 6 의 차이
a, b = input().split()
# a_max, b_max = ''.join(list(a)[:]), ''.join(list(b)[:])
if '5' in a:
    a_max = a.replace('5', '6') # replace 를 하면 주소값이 바뀐다/str은 immutable(변경불가) 하기때문
else:
    a_max = a
if '5' in b:
    b_max = b.replace('5', '6')
else:
    b_max = b
maxsum = int(a_max)+int(b_max)

if '6' in a:
    a = a.replace('6', '5')
if '6' in b:
    b = b.replace('6', '5')
minsum = int(a)+int(b)

print('{} {}'.format(minsum, maxsum))

# a = [1, 2, 3,4 ,5]
# b = a[:]
# b[2] = 7
# print(a)
# a = '123'
# b = str(a)
# print(id(a)==id(b))