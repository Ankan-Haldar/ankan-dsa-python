class Solution:

    def secondHighest(self, nums):

        first = -1
        second = -1

        for num in nums:

            if num > first:
                second = first
                first = num

            elif first > num > second:
                second = num

        return second


nums = [1,2,3,2,1]

obj = Solution()

print(obj.secondHighest(nums))


# Dry Run
# | num | first | second |
# | --- | ----- | ------ |
# | 1   | 1     | -1     |
# | 2   | 2     | 1      |
# | 3   | 3     | 2      |
# | 2   | 3     | 2      |
# | 1   | 3     | 2      |
