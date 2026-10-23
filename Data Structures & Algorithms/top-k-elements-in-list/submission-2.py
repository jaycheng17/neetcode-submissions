class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        sorted_seen = sorted(seen, key=lambda x: seen.get(x), reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_seen[i])
        
        return result

        

