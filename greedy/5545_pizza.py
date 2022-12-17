# 최고의 피자
def pizza(topping, a,b,c):
    totalc = c
    won = a
    maxc = totalc // won
    for d in topping:
        totalc += d
        won += b
        val = totalc//won
        if val >= maxc:
            maxc = val
        else:
            totalc -= d
            won -= b
    return maxc

n = int(input())
a, b = map(int, input().split())
c = int(input())
topping = []
for _ in range(n):
    topping.append(int(input()))
topping.sort(reverse=True)
print(pizza(topping, a,b,c))