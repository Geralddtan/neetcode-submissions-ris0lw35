class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hash_set = set()
        length = 0
        while r < len(s):
            if s[r] not in hash_set:
                hash_set.add(s[r])
                length = max(length, len(hash_set))
                r+=1
            else:
                while s[r] in hash_set:
                    hash_set.remove(s[l])
                    l+=1
                
        return length

