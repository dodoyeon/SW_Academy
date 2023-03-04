# 둘만의 암호
def solution(s, skip, index):
    dictionary = list(range(97, 123))
    skip = list(map(ord, skip))
    for i in skip:
        dictionary.remove(i)
    answer = ''
    for c in s:
        val = dictionary.index(ord(c))+index
        while val >= len(dictionary):
            val -= len(dictionary)
        answer += chr(dictionary[val])
    return answer

s = input()
skip = input()
index = int(input())
print(solution(s, skip, index))