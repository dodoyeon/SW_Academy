# 이상한 문자 만들기
def solution(s):
    answer = ''
    num = 0
    for c in s:
        val = ord(c)
        if (65<=val<=90)or(97<=val<=122):
            if num%2 == 0:
                if val >= 97:
                    answer += chr(val-32)
                else:
                    answer += c
            else:
                if val >= 97:
                    answer += c
                else:
                    answer += chr(val+32)
            num += 1
        else:
            answer += c
            num = 0
    return answer

def answersheet(str):
    answer = ''
    for s in str.split():
        for i, c in enumerate(s):
            if i%2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
    return answer

def answersheet2(str):
    ans = ' '.join(map(lambda x: ''.join([c.lower() if i%2 else c.upper() for i, c in enumerate(x)]), str.split()))
    return ans

print(answersheet2('TRY HELLO WORLD'))
print(answersheet2('try hello world'))
print(answersheet2('try hEllO wORlD'))