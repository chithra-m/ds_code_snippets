
def quick_sort(A, start, end):
    if start >= end:
        return
    pivot_index = partition(A,start,end)
    quick_sort(A,start,pivot_index-1)
    quick_sort(A, pivot_index+1, end)
    

def partition(A, start, end):
    pivot = A[start]
    i = start + 1
    j = end

    while True:
        while i <= j and A[i] <= pivot:
            i += 1 
        while i <= j and A[j] >= pivot:
            j -= 1 

        if i <= j:
            A[i] , A[j] = A[j], A[i]
        else:
            break
    
    A[start] , A[j] = A[j] , A[start]
    
    return j

A = [50,20,10,90,80,20,40,70]
print(A)