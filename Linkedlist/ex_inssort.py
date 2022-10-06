# 새로 리스트를 만들지 않고 sort 하는 방법 (메모리를 덜씀)
def original_insert(l):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -=1
        l[j+1] = key

# 새로 result 리스트를 만들어서 정렬하는 방법
def find_idx(l, x):
    idx = 0
    for i in l:
        if i < x:
            idx +=1
    return idx

def insert_sort(l):
    result = [l[0]]
    for i in range(1, len(l)):
        idx = find_idx(result, l[i])
        result.insert(idx, l[i])
    return result

print(insert_sort([3,5,1,9,2,6,8,7]))
print(original_insert([3,5,1,9,2,6,8,7]))