def solve(s,t):
    set1, set2 = set(), set()
    # set2 = set()
    for i in range(len(s)):
        set1.add(s[i])
        set2.add(t[i])
    print(set1)
    print(set2)
    if (len(set1)== len(set2)):
        return "true"
    return "false"
   
   
s = "egg"
t = "add"

s= "foo"
t = "bar"
print(solve(s,t))