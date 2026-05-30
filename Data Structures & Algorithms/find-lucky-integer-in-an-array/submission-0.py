class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        for i in arr:
            freq[i] = freq.get(i,0) + 1


        ans = -1

        for num,count in freq.items():
            if num == count:
                ans = max(num,ans)

        return ans
        
        