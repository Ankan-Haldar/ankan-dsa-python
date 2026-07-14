class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001
        for num in arr1:
            count[num] += 1
        ans = []
        for num in arr2:
            while count[num] > 0:
                ans.append(num)
                count[num] -= 1
        for i in range(1001):
            while count[i] > 0:
                ans.append(i)
                count[i] -= 1
        return ans