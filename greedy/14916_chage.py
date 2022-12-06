# 거스름돈
def cal(n):
    nam = n % 5
    nam_2 = nam%2
    mok = n//5
    if nam_2 ==0:
        num = mok + nam//2
        n = 0
    elif n>=5 and nam_2 == 1:
        num = (mok - 1) + (nam+5)//2
    else:
        return -1
    return num
n = int(input())
num = 0
print(cal(n))