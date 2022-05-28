#Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# def implementing_queue_using_two_stack(arr):
#     stack1=[]
#     stack2=[]
#     w=[]
#     for i in range(len(arr)):
#         stack1.append(arr[i])
#     for i in range(len(arr)):
#         g=stack1.pop()
#         stack2.append(g)
#     for i in range(len(arr)):
#         j=stack2.pop()
#         w.append(j)

#     return stack1,stack2,w


# arr=[1,2,3,4,5,6,7,8,9]
# s,w,r=implementing_queue_using_two_stack(arr)
# print(s)
# print(w)
# print(r)
class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,data):
        self.s1.append(data)
    def dequeue(self):
        if len(self.s1)==0 and len(self.s2)==0:
            print("Q empty")
            return 
        elif len(self.s1)>0 and len(self.s2)==0:
            while len(self.s1):
                tmp=self.s1.pop()
                self.s2.append(tmp)
            return self.s2.pop()
        else:
            return self.s1.pop()

q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
