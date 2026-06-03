class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k %= n

        def helper(left,right):

            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1

        helper(0,n-1)
        helper(0,k-1)
        helper(k,n-1)