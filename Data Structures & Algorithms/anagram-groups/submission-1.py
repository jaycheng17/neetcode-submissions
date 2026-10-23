class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outer_list = {}
        for word in strs:
            count = [0]*26
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1 
            key = tuple(count)

            if key in outer_list:
                outer_list[key].append(word)
            else:
                outer_list[key] = [word]
        
        outer_list = list(outer_list.values())
        return outer_list

            
            
