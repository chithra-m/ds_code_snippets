def longestCommonPrefix(str1s):
        str1 = min(str1s)
        str2 = max(str1s)
        print(str1, str2)
        if str1 == str2:
            return str1
        
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                str1 = str1[:i]
        return str1

str1s = ["ab", "a"]
print(longestCommonPrefix(str1s))

