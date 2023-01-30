def solve(nums, target):    
    dictionary = {}
    for i in range(len(nums)):
        dictionary[nums[i]] = i 
    print(dictionary)        
    for i in range(len(nums)):
        a = nums[i]
        b = target - a 
        print("gf",a,b)
        if b in dictionary:
            print(a,b)
            if (i-1) != dictionary[b]-1:
                return [i, dictionary[b]] 

nums = [3,2,4]
target = 6
print(solve(nums, target))