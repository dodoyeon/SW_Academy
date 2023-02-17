# 파스칼 삼각형
def pascaltri(r, c, w):
    h = (r+w-1)
    d = [[0]*(i+1) for i in range(h)]
    # total = (h*(h+1)//2)
    # d = [0]*total
    # d[0], d[1], d[2] = 1, 1, 1
    d[0][0], d[1][0], d[1][1] = 1, 1, 1
    num = 0
    for i in range(h):
        if i == 0:
            d[0][0] = 1
        elif i == 1:
            d[1][0], d[1][1] = 1, 1
        for j in range(i+1):
            if j == 0 or j == i:
                d[i][j] = 1
            else:
                d[i][j] = d[i-1][j-1]+d[i-1][j]
            if (r<=i+1<=h) and (c<=j+1<=c-(r-i)+1):
                num += d[i][j]
    return num

r, c, w = map(int, input().split())
print(pascaltri(r, c, w))