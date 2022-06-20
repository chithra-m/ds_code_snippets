# s = input()
s = 'ABCD'
if len(s)==1:
    print(ord(s)-64)

val = 1

for i in range(0,len(s)-1):
    print(s[i])
    val *= 26*((ord(s[i]))-64)

print(26+(ord(s[len(s)-1])-64))
val += 26+(ord(s[len(s)-1])-64)
print(val)