class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hash_set = set(s[0])
        if len(s) == 1:
            return 1

        l, r = 0, 1
        max_length = 1
        while r < len(s):
            if s[r] not in hash_set:
                hash_set.add(s[r])
                max_length = max(len(hash_set), max_length)
                r += 1
            else:
                while s[l] != s[r]:
                    hash_set.remove(s[l])
                    l += 1
                hash_set.remove(s[l])
                l += 1
        
        return max_length
            

