import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrct = collections.Counter(arr)

        counts = sorted(arrct.values())

        for i, c in enumerate(counts):
            if k > c:
                k -= c
            else:
                return len(counts) - i - 1 if k == c else len(counts) - i