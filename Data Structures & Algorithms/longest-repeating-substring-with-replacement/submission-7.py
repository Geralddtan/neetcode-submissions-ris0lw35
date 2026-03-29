class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        max_length = 0
        hashmap = defaultdict(lambda: 0)
        while r < len(s):
            hashmap[s[r]] += 1
            if (r-l+1) - max(hashmap.values()) <= k:
                max_length = max(max_length, r-l+1)
                r+=1
            else:
                hashmap[s[l]] -= 1
                l += 1
                hashmap[s[r]] -= 1

        return max_length


s="AABABBA"