# 거스름돈
m = int(input())
nam = (1000-m)
num = 0
while nam != 0:
    if nam >= 500:
        num+=1
        nam -= 500
    elif nam >= 100:
        num += (nam//100)
        nam = nam % 100
    elif nam >= 50:
        num += (nam // 50)
        nam = nam % 50
    elif nam >= 10:
        num += (nam // 10)
        nam = nam % 10
    elif nam >= 5:
        num += (nam // 5)
        nam = nam % 5
    else:
        num += nam
        nam = 0
print(num)