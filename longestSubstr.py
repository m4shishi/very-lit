class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub = ""
        sub2 = ""
        a = list(strs[0])
        b = list(strs[1])
        c = list(strs[2])
        k = 0
        for i in range(len(a)):
            for j in range(len(b)):
                if(i+k) < len(a) and (j+k) < len(b) and a[i + k] == b[j + k]:
                    sub = sub + a[i+k]
                    k = k + 1
        k = 0
        for i in range(len(a)):
            for j in range(len(c)):
                if(i+k) < len(a) and (j+k) < len(c) and a[i + k] == c[j + k]:
                    sub2 = sub2 + a[i+k]
                    k = k + 1

        if sub == sub2:
            return sub
        else:
            return ""