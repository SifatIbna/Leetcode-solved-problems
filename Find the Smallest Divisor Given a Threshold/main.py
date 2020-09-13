import math


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        possible_vals = [value for value in range(1, threshold + 1)]

        def check(mid):
            val = mid

            sum_ = 0
            for num in nums:
                sum_ += math.ceil(num / val)

            if sum_ > threshold:
                return False
            else:
                return True

        l, r = 1, int(1e6)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l