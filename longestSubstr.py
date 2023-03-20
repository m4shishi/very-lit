def longestCommonPrefix(strs):
    sub = ""
    sub2 = ""
    a = list(strs[0])
    b = list(strs[1])
    c = list(strs[2])
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                sub = sub + a[i]
                print(sub)
            # else:
            #     break
    
    for i in range(len(a)):
        for j in range(len(c)):
            if a[i] == c[j]:
                #print("a[i]=",a[i])
                sub2 = sub2 + a[i]
                #print(sub2)
            else:
                sub2 = ""
    if sub in a and sub in b:
        print("we got ",sub)
    else:
        sub = ""
        print(sub)
        
    # if sub == sub2:
    #     return sub
    # else:
    #     return ""
  
longestCommonPrefix(['flowers','flows','fleas'])