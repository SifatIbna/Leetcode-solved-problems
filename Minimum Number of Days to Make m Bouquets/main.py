class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1

        def bouquet(mid):
            c, res = 0, 0

            for n in bloomDay:
                c = 0 if n > mid else c + 1
                if c == k:
                    res += 1
                    c = 0

            return res

        Day = sorted(set(bloomDay))
        low, high = 0, len(Day) - 1

        while low < high:
            mid = (low + high) // 2

            if bouquet(Day[mid]) < m:
                low = mid + 1
            else:
                high = mid
        return Day[high] if Day[high] >= m else -1
