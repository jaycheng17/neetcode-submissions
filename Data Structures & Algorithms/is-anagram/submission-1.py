class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters_dict = {}
        for c in s:
            if c in characters_dict:
               x = characters_dict[c] 
               characters_dict[c] = x + 1
            else:
                characters_dict[c] = 1
        for c in t:
            if c in characters_dict:
                x = characters_dict[c]
                characters_dict[c] = x - 1
            else: 
                return False
        for key in characters_dict:
            if characters_dict[key] != 0:
                return False
        return True