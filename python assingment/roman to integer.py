class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {"I":1,
                        "V":5,
                        "X":10,
                        "L":50,
                        "C":100,
                        "D":500,
                        "M":1000}
        n = len(s)
        res = roman_to_int[s[-1]]
        for i in range(n-2,-1,-1):
            if roman_to_int[s[i]]<roman_to_int[s[i+1]]:
                res-=roman_to_int[s[i]]
            else:
                res+=roman_to_int[s[i]]
        return res
