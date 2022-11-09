# 로프
def max_mass(mass, n):
    mass.sort(reverse=True)
    m = 0
    for i in range(n):
        new = mass.pop()
        new_m = new * (len(mass)+1)
        if new_m >= m:
            m = new_m
    return m
n = int(input())
mass = [int(input()) for _ in range(n)]
print(max_mass(mass, n))