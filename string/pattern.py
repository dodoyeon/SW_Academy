T = int(input())
def function(n,m):
	len_n = len(n)
	skip = {val: (len_n - i - 1) for i, val in enumerate(n)}
	end = len_n - 1
	out = 0
	while end <= len(m):
		if m[end] == n[-1]:
			for i in range(end, (end - len_n + 1), -1):
				if m[i] == n[i - (end - len_n + 1)]:
					out += 1
				else:
					end = skip[i]
			if out == len_n:
				return 1
			else:
				out = 0
		end += len_n
		if end > len(m):
			end = len(m)
	return 0

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
# 	n = input() # 패턴
# 	m = input() # 문장
# 	print('#{} {}'.format(test_case, function(n,m)))

for test_case in range(1, T + 1):
	n = input() # 패턴
	m = input() # 문장
	if n in m:
		out= 1
	else:
		out=0 # 이거도 답임..
	print('#{} {}'.format(test_case, out))

