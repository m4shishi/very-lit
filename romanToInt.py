class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        if ((len(s) == 1 or len(s) == 2) and s in roman.keys()):
            return roman[s]
        # elif(len(s) == 2):
        #     return roman[''.join(list(s)[0])] + roman[''.join(list(s)[1])]
        # if len(s) == 4:
        #     return roman[''.join(list(s)[0])] + roman[''.join(list(s)[1:])]
        s = list(s)
        sum = roman[s[0]]
        for i in range(0, len(s)-1):
            if roman[s[i]] > roman[s[i+1]] or roman[s[i]] == roman[s[i+1]]:
                sum+=roman[s[i+1]]
            else:
                sum = sum + roman[s[i+1]] - 2*roman[s[i]]
        return sum

        
        return 1