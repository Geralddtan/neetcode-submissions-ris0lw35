class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        hashmap = defaultdict(lambda: 0)

        while r < len(s):
            length = r-l+1
            hashmap[s[r]] += 1
            if length - max(hashmap.values()) <= k:
                res = max(res, length)
            else:
                while (r-l+1) - max(hashmap.values()) > k:
                    hashmap[s[l]] -= 1
                    l+=1
            r+=1

        return res