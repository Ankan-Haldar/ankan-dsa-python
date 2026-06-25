from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


# Main Program
nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target element: "))

obj = Solution()
result = obj.search(nums, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")