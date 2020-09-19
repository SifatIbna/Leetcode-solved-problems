from itertools import permutations

mod = 10 ** 9 + 7


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        #         sum_ = 0
        #         temp_sum_ = 0
        #         perm = permutations(nums)
        #         for i in list(perm):
        #             for val in requests:

        #                 temp_sum_ += sum(i[val[0]:val[1]+1])

        #             if temp_sum_ > sum_:
        #                 sum_ = temp_sum_
        #             temp_sum_ = 0

        #         return sum_ % (10**9 + 7)
        n = len(nums)
        arr = [0] * (n + 1)  # add extra element for handel n+1 case
        for i, j in requests:
            arr[i] += 1
            arr[j + 1] -= 1

        for i in range(1, n + 1):
            arr[i] += arr[i - 1]

        arr = arr[:n]  # remove extra element
        nums.sort()
        arr.sort()

        ans = 0
        for i in range(n):
            ans += nums[i] * arr[i]

        return ans % mod