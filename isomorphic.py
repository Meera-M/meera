def isIsomorphic(s, t):
    s_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict.keys() and s_dict[s[i]] != t[i]:
            print("False")
        s_dict[s[i]] = t[i]
    print("True")
isIsomorphic('mee','abc')
