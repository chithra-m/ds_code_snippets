# # # class Queue:
    
# # #     def __init__(self):
# # #         self.queue = []
# # #         self.top = None 
# # #         self.size = 0 
    
# # #     def insert(self, value):
# # #         self.queue.append(value)
# # #         self.size += 1 
    
# # #     def remove(self):
# # #         if self.size > 0:
# # #             self.queue.pop(0)
# # #             self.size -= 1
# # #         else:
# # #             return 
    
# # #     def print(self):
# # #         for i in self.queue:
# # #             print(i)
            

# # # q = Queue()
# # # q.insert(5)
# # # q.insert(15)
# # # q.insert(10)
# # # q.remove()
# # # q.print()


# # a = [0,1,1,2,1,0]
# # 0,0,1,1,0,0,
# # i = 0
# # j = 0
# # k = len(a) - 1

# # while j < k:
# #     if a[j] == 1:
# #         j += 1
# #     elif a[j] == 0:
# #         a[i], a[j] = a[j], a[i]
# #         i += 1
# #         j += 1
# #     else:
# #         a[j], a[k] = a[k], a[j]
# #         j += 1
# #         k -= 1
# # print(a)


# class Node():
#     def __init__(self,val):
#         self.node = val 
#         self.next = None 

# class LinkedList():

#     def __init__(self):
#         self.head = None 
    
#     def insert(self, val):
#         if self.head:
#             self.head.next = Node(val)
#         else:
#             self.head = Node(val)
    
#     def reverse(self, head):
#         if head is None or head.next is None:
#             return head

#         # head.next =  self.reverse(head.next)        
#         # self.reverse(head.next).next = head
#         val =  self.reverse(head.next)  
#         head.next = val 
            
# 1 - 2 - 3 - 4 -> 5    
# {
# a : 1
# b : 2
# d : 3
# c : 4
# }



            4
        2       7 
    1       3
0 
#            3    
#       2       4   
#     1               7
# 0 

class binary_tree:

    def __init__(self) -> None:
        self.nodes = []
        self.size = len(self.nodes) 
