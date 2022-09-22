T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	n = input() # 패턴
	m = input() # 문장
	len_n = len(n)
	skip={val:(len_n-i-1) for i, val in enumerate(n)}
	end = len_n-1
	out = 0
	while end <= len(m):
		if m[end] == n[-1]:
			for i in range((end-len_n+1), end, -1):
				if m[i] != n[i-(end-len_n)]:
					break
					out = 1
		end += len_n
		if end >len(m):
			end = len(m)
	print('#{} {}'.format(test_case, out))