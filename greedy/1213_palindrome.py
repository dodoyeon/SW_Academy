# 팰린드롬 만들기
def palindrome_2(h_sort, len_h):
    count = 0
    res = [0]*len_h
    for i in h_sort:
        if len(i)%2 == 1:
            count += 1
            if count >= 2:
                return "I'm Sorry Hansoo"
            p = i.pop()
            res[len_h//2] = p
        for j in range(len(i)):
            for k in range(len_h):
                if res[k] == 0 and j%2==0:
                    res[k] = i[j]
                    break
                elif res[-(k+1)] == 0:
                    res[-(k+1)] = i[j]
                    break
    return ''.join(i for i in res)

h = list(input())
len_h = len(h)
h.sort() # string(알파벳)도 sort 가능하다
h_sort = []
p = h[0]
l = [p]
for i in range(1, len_h):
    if h[i] == p:
        l.append(p)
    else:
        p = h[i]
        h_sort.append(l)
        l = [p]
h_sort.append(l)
print(palindrome_2(h_sort, len_h))