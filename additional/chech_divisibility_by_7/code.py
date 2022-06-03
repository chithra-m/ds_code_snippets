
def div_by_7(n):
    if n == 0 or n == 7 or n == -7:
        return 'Yes'
    elif n>1 and n < 7 or n <= 10:
        return 'no'
    else:
        digit = n % 10
        n //= 10
        n = abs(n - 2*digit)
        return div_by_7(n)
            
n = int(input())
print(div_by_7(n))
        

