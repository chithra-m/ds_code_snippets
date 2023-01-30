def solve(nums):
    if len(nums) <= 1:
        return nums
    count = 0
    i = 1
    j = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            count += 1
        i += 1
    return len(nums)-count

nums = [1,1,1,2,2,2,3,3,3,4,5]
print(solve(nums))