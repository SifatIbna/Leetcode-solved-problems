class Solution:
    def conquer(self, left, right):
        min_length = min(len(left), len(right))
        for i in range(min_length):
            if left[i] != right[i]:
                return left[0:i]
        return left[0:min_length]

    def divide(self, strs, l, r):
        if l == r:
            return strs[l]
        else:
            mid = (l + r) // 2
            leftStr = self.divide(strs, l, mid)
            rightStr = self.divide(strs, mid + 1, r)
            return self.conquer(leftStr, rightStr)

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs is None or len(strs) == 0:
            return ""
        left = len(strs) - 1

        return self.divide(strs, 0, left)