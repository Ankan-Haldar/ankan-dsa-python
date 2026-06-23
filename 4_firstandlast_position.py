class Solution:

    # Find left-most occurrence
    def binarySearchLeft(self, nums, target):
        low, high = 0, len(nums) - 1
        index = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                index = mid
                high = mid - 1   # move left
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    # Find right-most occurrence
    def binarySearchRight(self, nums, target):
        low, high = 0, len(nums) - 1
        index = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                index = mid
                low = mid + 1    # move right
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    # Main Function
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binarySearchLeft(nums, target)

        if left == -1:
            return [-1, -1]

        right = self.binarySearchRight(nums, target)

        return [left, right]


# Example
nums = [5,7,7,8,8,10]
target = 8

obj = Solution()
print(obj.searchRange(nums, target))