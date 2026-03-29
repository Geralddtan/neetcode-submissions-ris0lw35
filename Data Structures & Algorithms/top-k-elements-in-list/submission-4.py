class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num,0)

        sort = sorted(dic.items(), key = lambda x:-x[1])
        if len(sort) == 1:
            return [sort[0][0]]

        final_ls = []
        for i in range(k):
            final_ls.append(sort[i][0])
        return final_ls

