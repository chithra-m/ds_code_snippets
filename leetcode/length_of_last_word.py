
s = 'HELLO WORLD'
s="   fly me   to   the moon  "
count = 0
i = len(s) - 1
print(s[i])
if s[i] == ' ':
    while s[i] == ' ' and i >=0 :
        print(s[i],"adh")
        i = i -1 

while s[i] != ' ' and i >= 0:
    print(s[i])
    count += 1
    i = i-1 
    
print(count)