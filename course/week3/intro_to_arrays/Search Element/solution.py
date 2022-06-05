def main():
    t = int(input())
    list1 = []
    for i in range(t):                
        A = list(map(int, input().split()))
        B = int(input())
        del A[0]
        if B in A:
            print("1")
        else:
            print("0")

    return 0

if __name__ == '__main__':
    main()