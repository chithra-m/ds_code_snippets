def main():
    A = list(map(int,input().split()))
    del A[0]
    B = int(input()) % len(A)
    rev(A,0,len(A)-1)
    rev(A,0,B-1)
    rev(A,B,len(A)-1)  
    for i in A:
        print(i,end=" ")
    
    return 0

def rev(A,start,end):
    i = start
    j = end

    while(i<=j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
        i += 1
        j -= 1

if __name__ == '__main__':
    main()