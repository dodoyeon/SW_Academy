# 문서 검색
def search_index(doc, a, i):
    global num
    for j in range(len(a)):
        if a[j] != doc[i+j]:
            return i+1
    num += 1
    return i+len(a)

def search_a(doc, a):
    l = len(doc)
    l_a = len(a)
    i = 0
    while i < l:
        if a[0] == doc[i] and (l-i) >= l_a:
            i = search_index(doc, a, i)
        else:
            i += 1

doc = input()
a = input()
num = 0
search_a(doc, a)
print(num)

# 다른 solution
print(input().count(input()))