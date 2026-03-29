class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(lambda: 0)
        for num in nums:
            dic[num] += 1
        
        vals = dic.items()
        vals = sorted(vals, key = lambda x:-x[1])
        answer = []
        for i in range(k):
            answer.append(vals[i][0])
        return answer