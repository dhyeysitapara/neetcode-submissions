class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        while slow <= len(nums):

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = nums[0]

        while slow2 != slow:

            slow2 = nums[slow2]
            slow = nums[slow]

        return slow2





# slow = 1
# fast = 1



# slow = 2
# fast = 3


# slow = nums[slow] = 3
# fast = nums[nums[fast]] = 3

