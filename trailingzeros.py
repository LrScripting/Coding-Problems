Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...



#with factorial calculation using tail recursion:
def factorial(n, a=1):
    if n == 1:
        return a
    else:
        return factorial(n-1, n*a)


def zerosFac(n):
    c= 0
    l = list(reversed(str(factorial(n, 1))))
    print(l)
    for i in l:
        if int(i) < 1:
            c+=1
        else: 
            return c
            
 #without calculating factorial:
 
 def zeros(n):
    c = 0
    i = 5
    while n >= i:
        c += n // i
        i *= 5
    return c
print(zerosFac(30))
