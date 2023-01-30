import sys
sys.setrecursionlimit(1000000)

def sortArray(nums):
    def merge(first, second):
        i, j = 0, 0
        third = []

        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                third.append(first[i])
                i += 1
            else:
                third.append(second[j])
                j += 1
        
        while i < len(first):
            third.append(first[i])
            i += 1
        
        while j < len(second):
            third.append(second[j])
            j += 1
        
        return third            

    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    first = sortArray(nums[:mid])
    second = sortArray(nums[mid:])
    print(first)
    return merge(first, second)

nums = [2,5,1,3]
print(sortArray(nums))
i = j = 0
print(i,j)
