def mul3and5(number):
    def threeAndFive(x):
        if x % 3 == 0 or x % 5 == 0:
            return True
        else:
            return False
    list1 = list(range(number+1))
    list1 = list(filter(threeAndFive,list1))
    list2 = sum(list1)
    return list2
  



mul3and5(8456)
