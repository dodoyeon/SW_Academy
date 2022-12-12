N = int(input())
votes = [0] * N
for i in range(N):
    votes[i] = int(input())
minimum = sum(votes) // N + 1
res = minimum - votes[0]
print(res if res > 0 else 0)