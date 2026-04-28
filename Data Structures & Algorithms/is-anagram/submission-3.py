class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1 = defaultdict(lambda: 0)
        hashmap_2 = defaultdict(lambda: 0)

        for char in s:
            hashmap_1[char]+=1
        
        for char in t:
            hashmap_2[char]+=1
        
        if len(hashmap_1)!=len(hashmap_2):
            return False

        for key, value in hashmap_1.items():
            if hashmap_2[key] != value:
                return False

        return True