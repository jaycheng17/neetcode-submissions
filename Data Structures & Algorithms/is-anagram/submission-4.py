class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = {}
        letters2 = {}

        for char in s:
            if char not in letters1:
                letters1[char] = 1
            else:
                temp = letters1[char]
                letters1[char] = temp + 1
        for char in t:
            if char not in letters2:
                letters2[char] = 1
            else:
                temp = letters2[char]
                letters2[char] = temp + 1
        
        return (letters1 == letters2)