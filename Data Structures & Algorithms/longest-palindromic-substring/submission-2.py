class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        for i in range(len(s)):
            longest1 = self.expand(i,i,s) #odd
            longest2 = self.expand(i,i+1,s) #even
            if len(longest1) >= len(longest):
                longest = longest1
            if len(longest2) >= len(longest):
                longest = longest2

        return longest

    def expand(self,left,right,s) -> str:
        start = left
        max_len = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_len:
                start = left
                max_len = right - left + 1
            left -= 1 
            right += 1
            
        return s[start:max_len + start]