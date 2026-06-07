class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1


        sorted_items = sorted(freq.items(), key = lambda x:x[1], reverse = True)

        result = []

        for num,count in sorted_items[:k]:
            result.append(num)

        return result

        