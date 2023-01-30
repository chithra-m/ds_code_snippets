def solve(A):
    frequency = {}
    for i in A:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    print(frequency)
    count_odd = 0
    for key,value in frequency.items():
        print(key,value)
        if (value % 2) == 1:
            print(value)
            count_odd += 1
    if count_odd > 1:
        return 0 
    return 1

A = "inttnikjmjbemrberk"
A = "vnpbeutxfqxriiajoejjmtjcx"
print(solve(A))