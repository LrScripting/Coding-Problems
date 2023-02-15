#'hard' rated leetcode problem, where you take a string and return the length of the longest substring of valid parentheses.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lol = list(s)
        count = 0
        newlis = []
        for i in range(len(lol)):
            if lol[i] == '(':
                count+=1
            if lol[i] == ")" and count == 0:
                newlis.append("s")
                continue
            if lol[i] == ")":
                count-=1
            newlis.append(count)
        c = 0
        final = 0
        for i in newlis:
            if i == 's':
                if c > final:
                    final = c
                    c = 0
                else:
                    c = 0
            else:
                c+=1
        print(final)


lol = Solution()
lol.longestValidParentheses(')()())')
