class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        counter = 0
        res = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in hashset:
                counter += 1
                res = max(res, counter)
                hashset.add(s[r])
            else:
                while s[l] != s[r]:
                    print(l, r)
                    print(hashset)
                    hashset.remove(s[l])
                    counter -= 1
                    l+=1

                l+=1
            r+=1
        
        return res