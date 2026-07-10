class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x
        ans = 0


        while left <= right:

            mid = (left + right) // 2

            square = mid * mid

            if square <= x:

                ans = mid
                left = mid + 1

            else:
                right = mid - 1


        return ans
        