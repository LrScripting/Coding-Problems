
def genEvenFib(highestValue):
    n = 0
    n1 = 1
    list1 = [0, 1]
    while list1[-1] < highestValue:
        summed =  n + n1
        list1.append(summed)
        n = n1
        n1 = summed
    return sum(list(filter(lambda x: (x % 2 == 0), list1)))
