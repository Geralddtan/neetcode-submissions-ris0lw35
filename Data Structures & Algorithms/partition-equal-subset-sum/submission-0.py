class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 == 1:
            return False

        target = total_sum//2

        hash_set = set()
        for num in nums:
            if num == target:
                return True
            
            new_set = set()
            for val in hash_set:
                if num + val == target:
                    return True
                new_set.add(num+val)

            hash_set = hash_set.union(new_set)
            if num not in hash_set:
                hash_set.add(num)
        
        return False
