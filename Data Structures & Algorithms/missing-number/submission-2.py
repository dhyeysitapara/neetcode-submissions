class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        actual_sum = sum(nums)

        original_sum = n * (n+1) // 2

        return original_sum - actual_sum
        