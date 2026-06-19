class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr = maxi = nums[0]

        for i in nums[1:]:

            curr = max(i,curr+i)
            maxi = max(maxi,curr)

        return maxi
        