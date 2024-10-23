class Solution(object):
    def twoSum(self, nums, target):
        num_first_index = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in num_first_index:
                return num_first_index[y], i
            num_first_index[x] = i

print(Solution([3, 3], 6)) # (1,2)
