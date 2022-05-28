#Given only a pointer/reference to a node to be deleted in a singly linked list, how do you delete it?
class Node:
    def __init__(self,datavalue):
        self.datavalue=datavalue
        self.nextvalue=None
class Linkedlist:
    def __init__(self):
        self.headvalue=None
    def push(self,key):
        newnode=Node(key)
        newnode.nextvalue=self.headvalue
        self.headvalue=newnode
    def print(self):
        t=self.headvalue
        while t!=None:
            print(t.datavalue)
            t=t.nextvalue
def delete(specific_ptr):
    prev=specific_ptr
    if specific_ptr==None:
        return
    while specific_ptr.nextvalue!=None:
        specific_ptr.datavalue=specific_ptr.nextvalue.datavalue
        prev=specific_ptr
        specific_ptr=specific_ptr.nextvalue
    prev.next=None

ll=Linkedlist()
ll.push(2)
ll.push(3)
ll.push(7)
ll.push(1)
ll.push(3)
ll.print()
delete(ll.headvalue)
ll.print()

