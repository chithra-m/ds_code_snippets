def isValidSudoku(A):
    # for i in range(9):
    #     frequency = {}
    #     for j in range(9):
    #         if A[i][j] == '.':
    #             continue
    #         elif A[i][j] in frequency:
    #             return 0
    #         else:
    #             frequency[A[i][j]] = 1

    # for j in range(9):
    #     frequency = {}
    #     for i in range(9):
    #         if A[i][j] == '.':
    #             continue
    #         elif A[i][j] in frequency:
    #             return 0
    #         else:
    #             frequency[A[i][j]] = 1
    print("in")
    temp = dict()

    for i in range(9):
        for j in range(9):
            row = i//3 
            col = j //3
            s = str(row) + str(col)
            if s in temp and A[i][j] != '.':
                print("dh")
                if A[i][j] in temp[s]:
                    print(temp[s])
                    print("yes")
                    return 0
                temp[s].append(A[i][j])

            elif s not in temp and A[i][j] != '.':
                temp[s] = []                
                temp[s].append(A[i][j])
    print(temp)
    return 1


  



    return 1
# # A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# # A = [ "..5.....6", "....14...", ".........", ".....92..", "5....2...", ".......3.", "...54....", "3.....42.", "...27.6.." ]
# A = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
# A = ["123......","456......","789......",".........",".........",".........",".........""........."]
A = [ "..5.....6", "....14...", ".........", ".....92..", "5....2...", ".......3.", "...54....", "3.....42.", "...27.6.." ]
main=[]
for i in range(9):
    temp = []
    for j in range(9):
        temp.append(A[i][j])
    main.append(temp)

for i in range(9):
    for j in range(9):
        print('|',main[i][j],'',end='')
    print()
print(isValidSudoku(A))