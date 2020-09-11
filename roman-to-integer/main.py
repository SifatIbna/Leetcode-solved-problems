class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_list = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        val = 0
        length = 0

        while length < len(s):

            if length == (len(s) - 1) :
                val = val + symbol_list[s[length]]
                break
            elif symbol_list[s[length+1]] > symbol_list[s[length]] :
                val = val + (symbol_list[s[length+1]]-symbol_list[s[length]])
                length += 2
            else:
                val = val + symbol_list[s[length]]
                length += 1
        return val