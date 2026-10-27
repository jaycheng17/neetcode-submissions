class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def count(i) -> int:

            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:
                return 1
            if i in memo:
                return memo[i]
            if int(s[i:i+2]) > 26:
                memo[i] = count(i+1)
                return memo[i]

            else:
                memo[i] = count(i+1) + count(i+2)
                return memo[i]

        return count(0)