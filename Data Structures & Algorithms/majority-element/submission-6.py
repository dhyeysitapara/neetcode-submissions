class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = 0
        score = 0

        for i in nums:

            if score == 0:
                candidate = i

            if candidate == i:
                score += 1

            else:
                score -= 1 
        
        return candidate