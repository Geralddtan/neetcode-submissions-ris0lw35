class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        buckets = [[] for i in range(len(nums))]
        for key, value in hashmap.items():
            buckets[value-1].append(key)

        res = []
        num = 0
        for i in range(len(nums)-1, -1, -1):
            res.extend(buckets[i])
            num += len(buckets[i])
            if num >= k:
                break

        return res