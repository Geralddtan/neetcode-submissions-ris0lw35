class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        counter = [[] for i in range(len(nums)+1)]
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

        for key, value in dic.items():
            counter[value].append(key)

        print(counter)
        final_ls = []
        for index in range(len(counter)-1,0,-1):
            for n in counter[index]:
                final_ls.append(n)
                if len(final_ls) == k:
                    return final_ls
        return final_ls

        

