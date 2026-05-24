class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1

            if freq[i] == 2:
                return True
                break

        else:
            return False
            
