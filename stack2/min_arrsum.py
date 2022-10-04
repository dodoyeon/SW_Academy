checked = []
def min_arrsum(arr, n):
    result = 0
    for i in range(n):


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
