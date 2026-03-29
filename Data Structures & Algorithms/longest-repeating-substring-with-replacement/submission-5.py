class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(lambda: 0)
        res = 0
        l,r = 0,0
        while r < len(s):
            hashmap[s[r]] += 1
            if (r-l)+1 - max(hashmap.values()) <= k:
                res = max(res,r-l+1)
                print(res, l , r)
                r += 1
            else:
                hashmap[s[l]] -= 1
                r+=1
                l+=1
        return res

