class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num=0
        for i in range(len(s)-1):
            if sym_val[s[i]] < sym_val[s[(i+1)]]:
                num-=sym_val[s[i]]
            else:
                num+=sym_val[s[i]]
        return num+sym_val[s[-1]]
