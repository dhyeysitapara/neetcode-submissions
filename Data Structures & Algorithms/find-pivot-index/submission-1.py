class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left = 0

        total_sum = sum(nums)

        for i in range(len(nums)):

            if left == total_sum - left - nums[i]:
                return i
            
            left += nums[i]


        return -1
