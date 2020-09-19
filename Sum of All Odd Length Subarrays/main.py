class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_ = 0

        for i in arr:
            sum_ += i
        length = 3
        while length <= len(arr):

            for i in range(0,len(arr)):

                if length+i <= len(arr):

                    sum_ += sum(arr[i:length+i])

            length += 2
        return sum_