"""Scrambelies coding challenge kata, CodeWars:
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered.
"""

def scramble(s1, s2):
    s1l = list(s1)
    s2l = list(s2)
    for i in range(len(s2l)):
        if s2l[i] not in s1l:
            return False
    return True



