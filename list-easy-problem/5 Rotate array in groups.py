# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]




class Solution:

    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        for _ in range(k):
            last = nums[n - 1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
print(obj.rotate(nums, k))



# | Step              | Action      | Array           |
# | ----------------- | ----------- | --------------- |
# | Initial           | —           | [1,2,3,4,5,6,7] |
# | Store last        | last = 7    | [1,2,3,4,5,6,7] |
# | Shift right       | —           | [1,1,2,3,4,5,6] |
# | Put last at start | nums[0] = 7 | [7,1,2,3,4,5,6] |



# | Step              | Action      | Array           |
# | ----------------- | ----------- | --------------- |
# | Store last        | last = 6    | [7,1,2,3,4,5,6] |
# | Shift right       | —           | [7,7,1,2,3,4,5] |
# | Put last at start | nums[0] = 6 | [6,7,1,2,3,4,5] |



# | Step              | Action      | Array           |
# | ----------------- | ----------- | --------------- |
# | Store last        | last = 5    | [6,7,1,2,3,4,5] |
# | Shift right       | —           | [6,6,7,1,2,3,4] |
# | Put last at start | nums[0] = 5 | [5,6,7,1,2,3,4] |



# Time Complexity
# Outer loop runs:
# k times
# Inner loop runs:
# n times
# Total:
# O(n×k)

# Space Complexity
# O(1)