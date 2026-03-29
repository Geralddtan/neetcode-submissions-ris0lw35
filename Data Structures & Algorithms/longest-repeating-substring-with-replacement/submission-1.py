class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(lambda : 0)
        l,r = 0, 0
        result = 0

        while r < len(s):
            dic[s[r]] += 1
            while (r-l+1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1
            
            result = max(result, r-l+1)
            r+=1

        return result

