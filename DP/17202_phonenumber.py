# 핸드폰 번호 궁합
def phone(a, b):
    while len(a) > 1:
        d1, d2 = [], []
        if len(a) == len(b):
            for i in range(len(a)):
                d1.append((a[i]+b[i])%10)
            for i in range(len(b)-1):
                d2.append((b[i]+a[i+1])%10)
        else:
            for i in range(len(a)-1):
                d1.append((a[i]+b[i])%10)
            for i in range(len(b)):
                d2.append((b[i]+a[i+1])%10)
        a, b = d1, d2
    return 10*a[0]+b[0]

def phone_answersheet(a, b):
    new = [0]*16
    for i in range(8):
        new[2*i] = a[i]
        new[2*i+1] = b[i]
    while len(new) > 2:
        temp =[]
        for i in range(len(new)-1):
            temp.append((new[i]+new[i+1])%10)
        new = temp
    return 10*new[0]+new[1]

a = list(map(int, input()))
b = list(map(int, input()))
print('{0:02d}'.format(phone_answersheet(a, b)))
# 8 8 - 8 7 - 7 7 - 7 6
# 8 7 - 7 7 - 7 6 - 6 6 - 6 5 -..