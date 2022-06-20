class queue:
    def __init__(self) -> None:
        self.list1 = []
 
    def push(self, data):
        self.list1.append(data)
    
    def size(self):
        return len(self.list1)

    def max_element(self):
        if self.size() != 0:
            return self.list1[self.size()-1]    
        elif self.size() == 0:
            return 0
        
    def pop(self):
        if self.size() != 0:
            self.list1.pop(0)


def find_max(A,k):
    q = queue()   
    ans = []
    
    q.push(A[0])
    print("first",q.size())
    count = 0
    for i in range(1,len(A)-k+1):       
        
        if q.size() != 2*k + 1 and A[i] >= q.max_element():
            q.push(A[i])

        print("max", q.max_element(),count)
        print(q.list1)
        ans.append(q.max_element())
        
        count += 1
        if count == 2*k and q.size() != 0:
            q.pop()

            count = 1
    
    return ans


A = [6,8,9,2,1,5,3,7,9]
k = 1
print(find_max(A,k))



# class Queue:
#     def __init__(self):
#         self.list1 = []

#     # def push(self,data,k):
#     #     if len(self.list1) == 0:
#     #         print("rhaetjh")
#     #         self.list1.append(data)
#     #         print("top value",self.list1[len(self.list1)-1])
#     #         # print("len list", len(self.list1))

#     #     elif data > self.list1[len(self.list1)-1]:
#     #         print(data,"top value",self.list1[len(self.list1)-1])
#     #         if len(self.list1) == k*2+1:
#     #             self.list1.pop(0)
            
#     #         # print("ht")
#     #         # print(data, self.list1[len(self.list1)-1])
#     #         self.list1.append(data)
#     #         print("list",self.list1)

#     def pop(self):
#         self.list1.pop(0)

#     def push(self,data):
#         self.list1.append(data)

#     def get_max(self):
#         # print("max",self.list1[len(self.list1)-1])
#         return self.list1[len(self.list1)-1]
            

# def find_max(A,k):
#     ans = []
#     queue = Queue()

#     for i in range(0,k-1):
#         while len(queue.list1) != 0 and A[i] >= queue.get_max:
#            queue.pop()
#         queue.push(A[i])
   
#     queue.push(A[0],k)

    
#     # # print(ans)
#     # for i in range(1,len(A)-k+1):
#     #     print(A[i],ans)
#     #     queue.pop(0)
#     #     queue.push(A[i],k)
#     #     # ans.append(queue.get_max())
#     #     # print(A[i],ans)

#     return ans


