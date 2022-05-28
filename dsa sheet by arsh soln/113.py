# Given a linked list and an integer N, the task is to delete the Nth node from the end of the given linked list.
from itsdangerous import NoneAlgorithm


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
    def display(self):
        d=self.headvalue
        while d!=None:
            print(d.datavalue)
            d=d.nextvalue
    def deletenodefromend(self,head,n):
        fast=head
        slow=head
        for i in range(n):
            fast=fast.nextvalue
        if not fast:
            return head.nextvalue
        while fast!=None:
            fast=fast.nextvalue
            slow=slow.nextvalue
        slow.nextvalue=slow.nextvalue.nextvalue
        return head
L=Linkedlist()
L.push(1)
L.push(2)
L.push(3)
L.push(4)
L.deletenodefromend(L.headvalue,3)
L.display()