# #Implement Stack using Queues
#if use stack after inserting (1,2,3,4)->poping would be 4321
#so we will have to apply the same logic
#take two array(queue)q1,q2
#insert an element in q1
#push remainng of q2 in q1
#swap q1,q2
class stack:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def push(self,key):
        self.q1.append(key)
        for i in self.q2:
            self.q1.append(i)
        self.q2,self.q1=self.q1,self.q2
        self.q1=[]
    def pop(self):
        self.q2.pop()
    def top(self):
        return self.q2[-1]

s=stack()
s.push(1)
s.push(2)
s.push(4)
print(s.top())
s.pop()
print(s.top())

