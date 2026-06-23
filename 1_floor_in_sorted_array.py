# Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x. This element is called the floor of x. If such an element does not exist, return -1.

# Note: In case of multiple occurrences of floor of x, return the index of the last occurrence.


class Solution:
    def findFloor(self, arr, x):
        n = len(arr)
        low = 0
        high = n - 1
        res = -1  
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return res