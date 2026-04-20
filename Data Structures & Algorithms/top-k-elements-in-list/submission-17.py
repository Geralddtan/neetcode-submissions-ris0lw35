class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(lambda: 0)
        for num in nums:
            hashmap[num]+=1

        buckets = [[] for i in range(len(nums))]
        for key, value in hashmap.items():
            buckets[value-1].append(key)
        
        res = []
        index = len(buckets)-1
        while len(res) < k:
            res.extend(buckets[index])
            index -= 1
        
        return res
