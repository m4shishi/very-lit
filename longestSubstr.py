def longestCommonPrefix(strs):
    sub = ""
    sub2 = ""
    a = strs[0]
    b = strs[1]
    c = strs[2]
    k = 0
    for i in range(len(a)):
        for j in range(len(b)):
            while((i+k) < len(a) and (j+k) < len(b) and a[i + k] == b[j + k]):
                sub = sub + a[i+k]
                k = k + 1
    u = 0
    for i in range(len(a)):
        for j in range(len(c)):
            while((i+u) < len(a) and (j+u) < len(c) and a[i + u] == c[j + u]):
                sub2 = sub2 + a[i+u]
                u = u + 1
    
    if sub == sub2:
        print(sub2)
        return sub
    if sub in sub2:
        return sub
    elif sub2 in sub:
        return sub2
    return ""
    
print(longestCommonPrefix(['flower', 'flight', 'flow']))