# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.



class Solution:
    def thirdMax(self, nums):
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        for num in nums:
            if num == first or num == second or num == third:
                continue

            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

        if third == float('-inf'):
            return first

        return third


nums = [3,2,1,5,3,8,4,2]

obj = Solution()

print(obj.thirdMax(nums))







# Dry Run
# | num | Action           | first | second | third |
# | --- | ---------------- | ----- | ------ | ----- |
# | 3   | New first        | 3     | -inf   | -inf  |
# | 2   | New second       | 3     | 2      | -inf  |
# | 1   | New third        | 3     | 2      | 1     |
# | 5   | New first        | 5     | 3      | 2     |
# | 3   | Duplicate → skip | 5     | 3      | 2     |
# | 8   | New first        | 8     | 5      | 3     |
# | 4   | New third        | 8     | 5      | 4     |
# | 2   | Smaller than all | 8     | 5      | 4     |

