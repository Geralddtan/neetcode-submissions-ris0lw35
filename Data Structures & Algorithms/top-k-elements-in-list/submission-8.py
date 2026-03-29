class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        bucket = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            freq[num] += 1
        for num, count in freq.items():
            bucket[count].append(num)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            for val in bucket[i]:
                result.append(val)
                if len(result) == k:
                    return result

        return result

