# 1차원 배열 입력받기
# a, *b = map(int, input().split()) # input = 5 1 2 3 4 5
# print(a, b) # a=5 b=[1,2,3,4,5]

# 1차원 배열
a = [0]*10
a1 = [0 for _ in range(10)]
# print(a, a1)

# 2차원 배열
b = [[0] for _ in range(10)]
b1 = [[0]*2]*3 # 이거는 초기화가 되기는 하지만 사용 불가!!!
# print(b)

# 2차원 배열 입력받기
# l,a,b,c,d = [int(input()) for _ in range(5)]
# print(l,a,b,c,d)

# n,m = map(int, input().split())
# c = [list(map(int, input())) for _ in range(n)] # 101111이렇게들어오는경우->
# print(c)                                        # split()없으면 [1,0,1,1,1,1] 받는다

# d = [list(map(int, input().split())) for _ in range(n)] # 1 0 1 1 1 1 인경우
# print(d)

# 정렬 Sorting 하기 :오름차순
a = [5,1,7,4,6]
# print(a)
b = sorted(a) # a는 변경시키지 않고 반환값을 정렬해서 넘겨준다
a.sort()
# print(a) # a 자체가 오름차순으로 정렬된다.
# print(b)

# 내림차순 sorting
a.sort(reverse=True)
# print(a)

# 갑자기 어려워지는 정렬 기준 정하기
# [[3, 2], [7, 4], [3, 4], [5, 1], [5, -7]] 여기에서
l = [[3, 4], [7, 4], [3, 2], [5, 1], [5, -7]]
l.sort()
print(l) # [[3, 2], [3, 4], [5, -7], [5, 1], [7, 4]]

l.sort(key=lambda x: x[1]) # y 좌표에 대해 정렬
print(l)

l.sort(key=lambda x: (x[1], -x[0])) # lambda :익명함수 잠깐 쓰고 없앨 함수, 기본인자=x :다음에 함수내용나옴
print(l)

# 백준 10825 : 국영수
# n = int(input())
# score = []
# for _ in range(n):
#     name = [input.split()]
#
# name.sort(key=lambda x: (-x[1],x[2],-x[3],ord(x[0])))