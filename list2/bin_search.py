def recur_bin_search(x, start, end, num):
    if end - start <= 1:
        return num
    mid = int(((start+end)/2))
    if x < mid:
        end = mid # mid-1 틀림 왜?
        num += 1
        return recur_bin_search(x, start, end, num)
    elif x > mid:
        start = mid # mid +1
        num += 1
        return recur_bin_search(x, start, end, num)
    else:
        return num

def bin_search():
    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    end, a, b = map(int, input().split())
    # book = [i for i in range(1, num+1)]
    num_a = bin_search(a, 1, end, 0)
    num_b = bin_search(b, 1, end, 0)
    if num_a<num_b:
        out = 'A'
    elif num_a>num_b:
        out = 'B'
    else:
        out = 0
    print('#{} {}'.format(test_case, out))