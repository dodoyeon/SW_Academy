n, k = input().split()
num = 0
for i in range(int(n)+1):
    for j in range(60):
        for l in range(60):
            out = str(i)+str(j)+str(l)
            if k == '0' and len(out) != 6:
                num += 1
            elif k in out:
                num += 1
print(num)

# i, j, l = 10,20,3
# k = '0'
# out = str(i)+str(j)+str(l)
# if k == 0 and len(out) != 6:
#     print('True')
# elif k in out:
#     print('True1')