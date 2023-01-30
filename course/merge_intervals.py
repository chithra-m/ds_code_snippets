def solve(intervals, new_interval):
    temp = []

    for i in range(len(intervals)):
        if intervals[i][1] < new_interval[0]:
            temp.append(intervals[i])            
            
        elif intervals[i][0] > new_interval[1]:
            temp.append(new_interval)
            while i < len(intervals): 
                temp.append(intervals[i])
                i += 1
            return temp

        else:
            min1 = min(new_interval[0],intervals[i][0])
            max1 = max(new_interval[1], intervals[i][1])
            new_interval = [min1, max1]

    temp.append(new_interval)
    return temp

intervals = [[1,3], [6,9]]
new_interval = [2,5]
print(solve(intervals, new_interval))