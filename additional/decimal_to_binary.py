n = int(input())
binary = []
while n >= 1:
    binary.append(n % 2)
    n = n // 2

print(binary[::-1])