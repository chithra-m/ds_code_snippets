def heapify(A,i):
    
    largest = i
    left = 2 * i 
    right = (2 * i) + 1

    if left < len(A) and A[left] > A[i]:
        largest = left 

    if right < len(A) and A[right] > A[largest]:
        largest = right 

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A,largest)


def insert_heap(A,new_data):
    if len(A) == 0:
        A.append(new_data)
    else:
        A.append(new_data) 
       
    for i in range((len(A)//2)-1, -1, -1):
        heapify(A, i)   
        

def delete_heap(A,data):
    
    if A[0] == data:
        A[len(A)-1], A[0] = A[0], A[len(A)-1]
        A.pop()
    
    # heapify(A, 1) # doubt
    for i in range((len(A)//2)-1, -1, -1):
        heapify(A, i)  


def heap_sort(A):
    for i in range((len(A)//2)-1, -1, -1):
        heapify(A, i)

    # temp = []

    # while len(A) >= 1:
    #     temp.append(A[0])
    #     delete_heap(A,A[0])

    i = len(A)-1
    while i >=0 :
        A[0],A[i] = A[i], A[0]
        heapify(A,0)
        i -= 1
    return A


A = [6,5,8,2,0,22,37,90]
print(heap_sort(A))

# insert_heap(A,60)
# insert_heap(A,20)
# insert_heap(A,30)
# insert_heap(A,66)

# print(A)

# A = [50,45,35,33,16,25,34,12,10]
# delete_heap(A,50)
# print(A)