# 2016년
def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    mon = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day[(sum(mon[:a])+b)%7-1]

a, b = map(int, input().split())
print(solution(a, b))