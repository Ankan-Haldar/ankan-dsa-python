class Solution:

    def reverseArray(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1

        return nums


nums = [1,2,44,3,23,4,5]
obj = Solution()

print(obj.reverseArray(nums))




# dryrun

# | Step    | left | right | Swap    | Array After Swap  |
# | ------- | ---- | ----- | ------- | ----------------- |
# | Initial | 0    | 6     | —       | [1,2,44,3,23,4,5] |
# | 1       | 0    | 6     | 1 ↔ 5   | [5,2,44,3,23,4,1] |
# | 2       | 1    | 5     | 2 ↔ 4   | [5,4,44,3,23,2,1] |
# | 3       | 2    | 4     | 44 ↔ 23 | [5,4,23,3,44,2,1] |
