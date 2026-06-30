class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            sign = -1
        else:
            sign = 1

        temp = abs(x)
        reverse = 0

        while temp > 0:

            ld = temp % 10

            reverse = reverse * 10 + ld

            temp = temp // 10

        reverse *= sign

        if reverse <= -2**31 or reverse >= 2**31 - 1:
            return 0

        return reverse