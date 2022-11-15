# 관중석 -> 이게 BFS&DFS???는 모르겠고 최대공약수 이용.
def func(seat_list, visited, d1, d2):
    num = 0
    for i in range(d1, d2+1):
        idx = i - d1
        for j in range(i):
            if visited[idx][j] == False:
                visited[idx][j] = True
                num += 1
    return num

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

# d1, d2 = map(int, input().split())
# visited = {} # visited 를 dict 를 쓰면 시간초과가 나는 듯 하다ㅠㅜ
# seat_list = []
# for i in range(d1, d2 + 1):
#     ang = (360 // i)
#     l = []
#     for j in range(i):
#         angle = j * ang
#         if angle != 360:
#             visited[angle] = False
#             l.append(angle)
#     seat_list.append(l)

# mem = []
# num = 0
# for i in range(d1, d2 + 1):
#     ang = (360 // i)
#     for j in range(i):
#         angle = j * ang
#         if angle not in mem: # 이거 때문에 시간이 오래걸려서 틀리는것 같다.
#             num += 1
#             mem.append(angle)

# 최대공약수로 풀이해야함.

# 이 방식은 c++ 하는 사람이 알려줬는데 역시 for를 2개 쓰고 그래서그런지 시간초과 19점
# l = set()
# for i in range(d1, d2+1):
#     ang = 1/i
#     for j in range(i):
#         l.add(ang*j)
# print(len(l))

# 최대공약수 사용 방법
# 이 방법은 그냥 틀렸다. 예를 들면 1 10 의 예시에서 2와10 사이 최대공약수로
# 2/10 4/20 6/10 8/10 을 제외했는데
# 4와10 사이 최대공약수로 4/10 8/10 을 한번 더 제외시키기때문에 원래 답보다 적은값을 얻는다.
# from math import gcd
# num = ((d1+d2)*(d2-d1+1))//2 -(d2-d1)
# for i in range(d2, d1, -1):
#     for j in range(d1, i):
#         num -= (gcd(i, j)-1)
# print(num)

def solve():
    a, b = map(int, input().split())
    arr = [[0] * b for _ in range(b)]
    ans = 0
    for i in range(a, b + 1):
        for j in range(1, i + 1):
            g = gcd(i, j)
            x, y = i // g, j // g # x=분모 y=분자
            if not arr[x-1][y-1]: # 1이 아니면 = 센 적이 없으면(visited)
                arr[x-1][y-1] = 1
                ans += 1
    print(ans)

solve()