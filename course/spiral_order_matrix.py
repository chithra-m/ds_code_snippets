def left_to_right(val,i,ans,A):
    j = 0
    # print("i",i,j)
    while j < A and ans[i][j] == 0:
        ans[i][j] = val
        val += 1
        j += 1

 
def top_to_bottom(val,j,start_row,ans,A): 
    i = start_row
    print(i,j,val)
    while i < A and ans[i][j] == 0:
        print("ij",i,j)
        ans[i][j] = val
        val += 1
        i += 1


def right_to_left(val,i,ans,A):
    j = A - 2
    # print(i,j,val)                                        
    while j >= 0 and ans[i][j] == 0:
        ans[i][j] = val
        val += 1
        j -= 1


def bottom_to_top(val,j,ans,A):
    i = A - 2
    # print(i,j,val)
    while i >= 0 and ans[i][j] == 0:
        ans[i][j] = val
        val+= 1
        i -= 1

def generateMatrix(A):
    ans = []
    start_row, start_col, end_row, end_col = 0,0,A-1,A-1
    for i in range(A):
        temp = []
        for j in range(A):
            temp.append(0)
        ans.append(temp)
    
    val = 1
    while val <= A*A:
        
        i = start_row
        left_to_right(val,i,ans,A)
        val += A
        start_row += 1
        print(ans)

        j = end_col
        top_to_bottom(val,j,start_row,ans,A)
        val += A - 1
        end_col -= 1
        print(ans)

        i = end_row
        right_to_left(val,i,ans,A)
        val += A -1
        end_row -= 1
        print(ans)

        j = start_col
        bottom_to_top(val,j,ans,A)
        val += 1
        start_col -= 1
        print(ans)

    return ans



A = 3
print(generateMatrix(A))
# 1 2 3
# 8 9 4
# 7 6 5

# 1   2   3  4
# 12  13  14  5
# 11         6
# 10  9   8  7        