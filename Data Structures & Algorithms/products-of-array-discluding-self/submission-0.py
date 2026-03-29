class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1] * nums[i])

        reversed_nums = nums[::-1]
        for i in range(len(reversed_nums)):
            if i == 0:
                postfix.append(reversed_nums[i])
            else:
                postfix.append(postfix[i-1] * reversed_nums[i])

        postfix = postfix[::-1]

        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[i+1])
            elif i == len(nums)-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * postfix[i+1])

        return result
             
