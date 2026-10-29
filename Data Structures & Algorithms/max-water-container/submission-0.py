class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            area = min(heights[left],heights[right]) * (right - left)
            if area > highest:
                highest = area
            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1
                right -= 1

        return highest
        