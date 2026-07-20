class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count = {}
        for i in nums:
            if i in number_count:
                count = number_count[i]
                number_count[i] = count+1
            else:
                number_count[i] = 1
        val_based_rev = {k: v for k, v in sorted(number_count.items(), key=lambda item: item[1], reverse=True)}
        res = []
        count = 1;
        for key in val_based_rev:
            if count > k:
                break
            res.append(key) 
            count += 1
        
        return res
            