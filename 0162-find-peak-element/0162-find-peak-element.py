class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # Peak is on the left side (including mid)
            if nums[mid] > nums[mid + 1]:
                high = mid
            # Peak is on the right side
            else:
                low = mid + 1

        return low