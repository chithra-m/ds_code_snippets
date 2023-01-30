def remove_element(nums, val):
    count = 0
    i = 0
    j = len(nums) - 1
    
    while i < len(nums) and j >= 0 and i < j: 
        if nums[i] == val:
            while j >= 0 and i < j:
                print(nums[i],nums[j])
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                    count += 1
                    j -= 1
                    i += 1
                    break
                j -= 1 
                count+=1
                print(nums)
        else:
            count += 1
            i += 1
    print(nums)            
    print(count)
    return count

nums = [0,1,2,2,3,0,4,2]
val = 2
nums = [3,2,2,3]
val = 3
print(remove_element(nums, val))