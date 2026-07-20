class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                answer = [seen[nums[i]],i]
            difference = target - nums[i]
            seen[difference] = i

        return answer

