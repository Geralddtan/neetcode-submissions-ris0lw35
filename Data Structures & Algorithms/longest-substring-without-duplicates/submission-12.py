class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        subset = set(list(s[0]))
        res = 1
        while r < len(s):
            if s[r] not in subset:
                subset.add(s[r])
                res = max(res, len(subset))
                r+=1
            else:
                while s[r] in subset:
                    subset.remove(s[l])
                    l+=1
        
        return res

