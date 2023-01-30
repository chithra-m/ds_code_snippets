def binary_search(nums, l, r):
    if l > r:
        return 
    while l < r:
        mid = (l + r) // 2
        print(nums[mid - 1], nums[mid])
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            print("case 1")
            return mid  
        elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
            print("case 2")
            r = mid - 1
        else:
            print("case 3",l,r)
            l = mid + 1 
    return - 1

nums = [1,2,1,3,5,6,4]
# Output: 5
binary_search(nums, 0, len(nums) - 1)

from collections import deque 

# class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    # def solve(self, A):
A = [4]
root = A[0]
q = deque()
q.append(root)
i = 1
print(q)
        # while(len(q) != 0):
        #     cur = q.popleft()
        #     if(cur == None):
        #         continue
        #     val_left = A[i]
        #     val_right = A[i+1]
        #     i += 2
        #     if(val_left == -1):
        #         cur.left = None
        #     else:
        #         cur.left = TreeNode(val_left)
        #     if(val_right == -1):
        #         cur.right = None
        #     else:
        #         cur.right = TreeNode(val_right)
        #     q.append(cur.left)
        #     q.append(cur.right)
        # return root