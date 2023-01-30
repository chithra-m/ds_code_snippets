def solve(A, B):
    window_size = 0
    for i in range(len(A)):
        if A[i] <= B:
            window_size += 1
    print(len(A), window_size)
    if window_size == len(A):
        return 0 
    crct = 0
    wrong = 0
    
    for i in range(window_size):
        if A[i] <= B:
            crct += 1
        else:
            wrong += 1 
    min_swap = wrong
    print(min_swap)

    for i in range(window_size, len(A)):
        # print('i',i)
        if A[i-window_size] <= B:
            crct -= 1
        else:
            wrong -= 1

        if A[i] <= B:
            crct += 1
        else:
            wrong += 1 

        min_swap = min(wrong, min_swap)
        print(i, min_swap)

    return min_swap 
    

# A = [1, 12, 10, 3, 14, 10, 5]
# B = 8
# A = [5, 17, 100, 11]
# B = 20
# A = [ 52, 7, 93, 47, 68, 26, 51, 44, 5, 41, 88, 19, 78, 38, 17, 13, 24, 74, 92, 5, 84, 27, 48, 49, 37, 59, 3, 56, 79, 26, 55, 60, 16, 83, 63, 40, 55, 9, 96, 29, 7, 22, 27, 74, 78, 38, 11, 65, 29, 52, 36, 21, 94, 46, 52, 47, 87, 33, 87, 70 ]
# B = 19
A = [ 1932, 8692, 6019, 8005, 5159, 4687, 9436, 4938, 6868, 9019, 6392, 9361, 8824, 4726, 6998, 645, 8207, 3417, 3175, 5683, 872, 3982, 4739, 112, 6004, 6865, 3746, 7370, 9634, 4610, 796, 1472, 5105, 1049, 5247, 4945, 7048, 3467, 2429, 4206, 1660, 4345, 4837, 904, 166, 1880, 1028, 9172, 4236, 1378, 5481, 5604, 1804, 2823, 5030, 839, 9263, 3461, 2651, 9118, 1333, 8063, 7359, 4867, 3022, 3697, 9767, 3467, 9058, 290, 6462, 6711, 4923, 3034, 2747, 2137, 193, 7794, 2580, 9418, 9285, 6058, 6508, 6310, 6883, 1700, 3323, 1258, 5352, 7824, 8772, 9705, 9261, 8335, 5168, 6386, 7760, 5499, 9030, 6458, 9022, 1729, 9974, 4165, 2205, 1120, 3014, 8943, 1477, 3820, 8127, 5342, 3509, 4250, 5529, 4962, 4571, 2381, 2396, 5724, 5835, 5813, 6997, 6203, 5849, 9222, 9126, 527, 7262, 6918, 1563, 2386, 823, 3695, 5849, 5052, 3456, 8938, 7116, 8024, 8753, 9050, 6923, 9869, 7660, 3646, 77, 1183, 4275, 1679, 1311, 1153, 6726, 4700, 305, 6193, 5897, 5777, 9074, 9348, 5423, 4249, 3970, 4687, 4800, 8476, 5714, 1831, 3741, 974, 4749, 1908, 9952, 2981, 5939, 7712, 4424, 8326, 6197, 7692, 7988, 9745, 966, 5467, 446, 4276, 635, 4032, 8848, 8229, 5970, 6545, 4680, 6347, 2420, 3646, 643, 4281, 6757, 628, 6456, 8222, 5938, 6464, 9726, 677, 7292, 691, 2261, 6725, 1183, 3438, 4448, 855, 2160, 8546, 293, 452, 2253, 9602, 3565, 8398, 573, 4020, 1102, 3852, 6643, 788, 2795, 7280, 1022, 3436, 9038, 3038, 5659, 909, 5467, 441, 8179, 5558, 1742, 2122, 8826, 9239, 5779, 6707, 6140, 5671, 7396, 1364, 7625, 9581, 5606, 8611 ]
B = 2850
print(solve(A,B))