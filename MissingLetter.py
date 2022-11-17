"""Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case."""


def find_missing_letter(chars):
    final = []
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']  
    arr2 = [i.capitalize() for i in arr]
    if chars[0] != chars[0].capitalize():
        l = arr.index(chars[0])
        lindex = arr.index(chars[-1])
    else:
        l = arr2.index(chars[0])
        lindex = arr2.index(chars[-1])
    while l < lindex:
        if chars[0] == chars[0].capitalize():
            if arr2[l] not in chars:
                final.append(arr2[l])
        else: 
            if arr[l] not in chars:
                final.append(arr[l])
        l+=1
    return str(final)[1:-1].strip(" ' ' ")
