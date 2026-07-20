class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        default = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            default[tuple(count)].append(s)
        return list(default.values())