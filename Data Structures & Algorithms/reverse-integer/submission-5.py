class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else: 
            sign = 1

        current = abs(x)

        reverse = 0

        while current > 0:
            ld = current % 10
            reverse = reverse * 10 + ld
            current = current // 10

        

        if reverse <= -2**31 or reverse >= 2**31 - 1:
            return 0

        return reverse * sign

        