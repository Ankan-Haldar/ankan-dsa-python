class Solution:

    def reverseInGroups(self, nums, k):

        n = len(nums)

        for i in range(0, n, k):

            left = i
            right = min(i + k - 1, n - 1)

            while left < right:

                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right -= 1

        return nums


nums = [1,2,3,4,5,6,7,8]

k = 3

obj = Solution()

print(obj.reverseInGroups(nums, k))


# Group 1 → [1,2,3]
# | Step    | left | right | Swap  | Array             |
# | ------- | ---- | ----- | ----- | ----------------- |
# | Initial | 0    | 2     | —     | [1,2,3,4,5,6,7,8] |
# | 1       | 0    | 2     | 1 ↔ 3 | [3,2,1,4,5,6,7,8] |

# Group 2 → [4,5,6]
# | Step    | left | right | Swap  | Array             |
# | ------- | ---- | ----- | ----- | ----------------- |
# | Initial | 3    | 5     | —     | [3,2,1,4,5,6,7,8] |
# | 1       | 3    | 5     | 4 ↔ 6 | [3,2,1,6,5,4,7,8] |


# Group 3 → [7,8]
# | Step    | left | right | Swap  | Array             |
# | ------- | ---- | ----- | ----- | ----------------- |
# | Initial | 6    | 7     | —     | [3,2,1,6,5,4,7,8] |
# | 1       | 6    | 7     | 7 ↔ 8 | [3,2,1,6,5,4,8,7] |



# Time Complexity
# Each element is visited once.

# O(n)

# Space Complexity
# No extra array used.

# O(1)