# 기타줄
def buy(n, single_min, pack_min):
    buy_pack = n//6
    nam = n%6
    min_l = []
    min_l.append(pack_min*(buy_pack+1))
    min_l.append(pack_min*buy_pack + single_min*nam)
    min_l.append(single_min*n)
    return min(min_l)

    # min_p = 1000000
    # min_s = 1000000
    # for i in :
    #     now = i[0]*buy_pack + i[1]*nam
    #     if min_p > now:
    #         min_p = now
    # for i in brand_s:
    #     now = n*i[1]
    #     if min_s > now:
    #         min_s = now

n, m = map(int, input().split())
brand_p = []
brand_s = []
single_min = 1000
pack_min = 6000
for _ in range(m):
    b = list(map(int, input().split()))
    # if b[0] > b[1]*6:
    #     brand_s.append(b)
    # else:
    #     brand_p.append(b)
    if b[1] < single_min:
        single_min = b[1]
    if b[0] < pack_min:
        pack_min = b[0]

print(buy(n, single_min, pack_min))