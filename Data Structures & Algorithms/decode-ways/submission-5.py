class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def count(substring) -> int:
            n = len(substring)
            if n == 0:
                return 1
            if substring[0] == '0':
                return 0
            if n == 1:
                return 1
            if n in memo:
                return memo[n]
            if int(substring[0:2]) > 26:
                memo[n] = count(substring[1:])
                return memo[n]

            else:
                memo[n] = count(substring[1:]) + count(substring[2:])
                return memo[n]

        return count(s)