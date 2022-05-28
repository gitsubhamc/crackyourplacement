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
    def reverse(self):
        prev=None
        current=self.headvalue
        while current!=None:
            next=current.nextvalue
            current.nextvalue=prev
            prev=current
            current=next
        self.headvalue=prev
    def print(self):
        d=self.headvalue
        while d!=None:
            print(d.datavalue)
            d=d.nextvalue
ll=Linkedlist()
ll.push(3)
ll.push(4)
ll.push(5)
ll.print()
ll.reverse()
ll.print()