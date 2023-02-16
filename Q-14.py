#14
n = [int(x) for x in input().split()]
for x in n:
    if n.count(x) == 1:
        print(x,end=' ')
