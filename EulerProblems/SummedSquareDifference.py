def squareddiff(n):
    l = list(range(1,n+1))
    lsum = sum(l)
    lsumSqr = lsum * lsum
    l2 = list(map(lambda x: (x*x), l))
    l2sum = sum(l2)
    return lsumSqr - l2sum
 
print(squareddiff(20))
