def longestCommonPrefix(A):
    smaller = min(A)
    bigger = max(A)

    for i in range(len(smaller)):
        if smaller[i] != bigger[i]:
            return smaller[:i]
        
    return smaller

A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abab", "ab", "abcd"]
print(longestCommonPrefix(A))