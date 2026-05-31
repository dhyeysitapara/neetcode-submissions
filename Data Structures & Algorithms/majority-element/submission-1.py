class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}
        n = len(nums)

        # nums = nums.sort()

        for i in nums:
            freq[i] = freq.get(i,0) + 1

            if freq[i] > n // 2:
                return i
        