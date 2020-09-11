class Solution:

    def reversed(self, x: int) -> int:
        val = 0
        while x > 0:
            val = val * 10 + x % 10
            x = x // 10
            if val > 2 ** 31 - 1 or val < -2 ** 31:
                return 0
        return val

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            if x == self.reversed(x):
                return True
            return False

object = Solution()
print(object.isPalindrome(121))
