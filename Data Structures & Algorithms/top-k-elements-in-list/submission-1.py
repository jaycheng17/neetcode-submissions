class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for i in nums:
            if i in number_count:
                count = number_count[i]
                number_count[i] = count+1
            else:
                number_count[i] = 1
        for key in number_count:
            frequency[number_count[key]].append(key)
        res = []
        for i in range (len(frequency)-1, -1, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res