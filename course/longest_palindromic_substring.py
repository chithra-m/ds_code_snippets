def expand(A,p1,p2):
    s = ""
    while (p1 >= 0 and p2 < len(A) and A[p1] == A[p2]):
        p1 -= 1
        p2 += 1

    return A[p1+1:p2]


def longestPalindrome(A):
    max_len = 0
    max_string = ""
    for i in range(len(A)):
        cur_str = expand(A,i,i)
        if len(cur_str) > max_len:
            max_len = len(cur_str)
            max_string = cur_str
        cur_str = expand(A,i,i+1)
        if len(cur_str) > max_len:
            max_len = len(cur_str)
            max_string = cur_str
        
    return max_string
    
A = "aaaabaaa"
A = "acca"
print(longestPalindrome(A))