class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for c in s:
            c = c.lower()
            count[ord(c) - ord('a')] += 1
        for c in t:
            c = c.lower()
            count[ord(c) - ord('a')] -= 1
        for x in count:
            if x != 0:
                return False

        return True;