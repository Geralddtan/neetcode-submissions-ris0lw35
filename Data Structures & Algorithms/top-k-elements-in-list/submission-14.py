class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(lambda: 0)
        for num in nums:
            hashmap[num] += 1

        max_count = max(hashmap.values())
        store = [[] for i in range(max_count+1)]
        for key, value in hashmap.items():
            store[value].append(key)

        res = []
        for i in range(len(store)-1,-1,-1):
            if store[i]:
                res.extend(store[i])
            if len(res) == k:
                return res
        
        return res

            
