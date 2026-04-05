class Solution:
    def reverseSubArray(self, arr, l, r):
        l -= 1
        r -= 1
        self.func(arr, l, r)
        return arr
    def func(self, arr, left, right):
        if left >= right:
            return
        arr[left], arr[right] = arr[right], arr[left]
        self.func(arr, left + 1, right - 1)
    