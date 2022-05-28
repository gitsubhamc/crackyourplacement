# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
class Node:
    def __init__(self,data):
        self.datavalue=data
        self.nextvalue=None
class Linkedlist:
    def __init__(self):
        self.headvalue=None
    def push(self,key):
        newnode=Node(key)
        newnode.nextvalue=self.headvalue
        self.headvalue=newnode
    def print(self):
        s=self.headvalue
        while s!=None:
            print(s.datavalue)
            s=s.nextvalue
            
ll=Linkedlist()
l2=Linkedlist()
ll.push(3)
ll.push(4)
ll.push(2)
ll.push(7)
l2.push(4)
l2.push(6)
l2.push(5)
ll.print()
l2.print()

    