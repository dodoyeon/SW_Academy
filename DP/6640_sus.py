# Suspicious Stocks
def stock(d,m,l):
    d = [0]*d
    visited = [False]*d
    return 0

while True:
    d = input()
    if d == '0':
        break
    d, m = map(int, d.split())
    l = list(map(int, input().split()))
    out = stock(d,m,l)
    if out <= 0:
        print(0)
    else:
        print(out)