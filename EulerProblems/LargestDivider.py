#find largest Number which is divisible by 1-n
def largest(x):
    l = list(range(1,x+1))
    c = x+1
    final = 0
    while final < 1:
        l1 = list(filter(lambda x: (c % x == 0), l))
        if len(l1) == len(l):
            final = c
        else:
            c+=1
    return final

print(largest(7))

