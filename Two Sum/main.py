class Solution:

    def twoSum(self, nums, target):
        traversed = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in traversed:
                return [traversed[diff], i]
            if v not in traversed:
                traversed[v] = i
        return []


object = Solution()
print(object.twoSum([2, 7, 11, 15], 9))
