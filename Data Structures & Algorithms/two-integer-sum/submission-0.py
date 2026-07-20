class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in hashmap:
                x = hashmap[difference]
                result = [x,index]
                return result
            else:
                hashmap[nums[index]] = index

        return result