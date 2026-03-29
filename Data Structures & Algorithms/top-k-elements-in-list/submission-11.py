class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(lambda: 0)
        for num in nums:
            dic[num] += 1
        
        bucket = [[] for i in range(len(nums)+1)]
        for key, value in dic.items():
            bucket[value].append(key)
        
        result = []
        for i in range(len(bucket)-1,0,-1):
            if bucket[i] != []:
                result.extend(bucket[i])
            if len(result) == k:
                return result
        
        return result


