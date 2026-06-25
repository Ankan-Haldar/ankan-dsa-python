class Solution:
    # ---------- helper: first index with value >= target ----------
    def lower_bound(self, nums, target):
        n = len(nums)
        lb  = -1              # default when target isn't found
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb  = mid          # potential first position
                high = mid - 1     # keep searching left half
            else:                  # nums[mid] < target
                low = mid + 1
        return lb

    # ---------- helper: first index with value > target ----------
    def upper_bound(self, nums, target):
        n = len(nums)
        ub  = n               # default when all elements <= target
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub  = mid          # potential upper bound
                high = mid - 1     # look further left
            else:                  # nums[mid] <= target
                low = mid + 1
        return ub

    # ---------- driver: count occurrences of target ----------
    def countFreq(self, arr, target):
        lb = self.lower_bound(arr, target)
        # if target never appears, quick exit
        if lb == -1 or arr[lb] != target:
            return 0

        ub = self.upper_bound(arr, target)
        return ub - lb            # total number of occurrences