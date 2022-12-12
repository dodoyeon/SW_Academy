line = input()
count = 0
line = line.replace('XXXX','AAAA')
line = line.replace('XX','BB')
if 'X' in line:
    print(-1)
else:
    print(line)