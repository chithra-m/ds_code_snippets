import sys
def main():
    A = list(map(int,(input().split())))
    max = A[1]
    min = A[1]
    for i in range(2,len(A)):
        if A[i] > max:
            max = A[i]
        if A[i] < min:
            min = A[i]
    print(max,min)   
    return 0

if __name__ == '__main__':
    main()