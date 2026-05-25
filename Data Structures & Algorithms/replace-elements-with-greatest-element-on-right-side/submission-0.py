class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_compare = -1

        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = max_compare
            max_compare = max(temp,max_compare)

        return arr

        