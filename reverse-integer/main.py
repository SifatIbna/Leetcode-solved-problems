class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        temp = x
        if x < 0 :
            temp = temp *(-1)
        while temp > 0 :
            rev_num = rev_num*10 + temp%10
            temp = temp//10
            if rev_num > 2**31-1 or rev_num < -2**31:
                 return 0 
        if x < 0 :
            return rev_num*(-1)
        else:
            return rev_num