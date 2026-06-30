class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = {}
        result = []

        for i in set(nums1):
            set1[i] = set1.get(i,0) + 1

        for i in set(nums2):
            if i in set1:
                result.append(i)


        return result
        