class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2 ):
            fixed = nums[i]
            if fixed == nums[i - 1] and i > 0:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = fixed + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([fixed,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1


                
        return result
