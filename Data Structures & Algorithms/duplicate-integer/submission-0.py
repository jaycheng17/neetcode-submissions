class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupeDict = {}
        for i in nums:
            if i in dupeDict:
                    return True
            dupeDict[i] = "T"
        
        return False;