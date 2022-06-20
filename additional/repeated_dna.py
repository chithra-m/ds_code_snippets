def solve(s:str):
    substrings = {}        
    ans = set()
    
    for i in range(0,len(s)-9):
        if s[i:i+10] in substrings:
            substrings[s[i:i+10]] += 1
            ans.add(s[i:i+10])
        else:
            substrings[s[i:i+10]] = 1
    
    return ans


    



s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAA"
print(solve(s))