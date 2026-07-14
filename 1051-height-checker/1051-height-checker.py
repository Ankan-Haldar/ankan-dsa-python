class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101

        for h in heights:
            count[h] += 1

        current = 1
        mismatch = 0

        for h in heights:
            while count[current] == 0:
                current += 1

            if h != current:
                mismatch += 1

            count[current] -= 1

        return mismatch