def tell(line):
    count= [False]*4
    for i in line:
        if i == 'U':
            count[0] = True
        elif i == 'C' and count[0] and not count[1]:
            count[1] = True
        elif i == 'P' and count[0] and count[1]:
            count[2] = True
        elif i == 'C' and count[0] and count[1] and count[2]:
            count[3] = True
            return 'I love UCPC'
    return 'I hate UCPC'
line = input()
print(tell(line))