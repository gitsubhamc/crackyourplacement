class Node:
    def __init__(self,data):
        self.datavalue=data
        self.nextvalue=None
def printlist(head):
    s=head
    while s!=None:
        print(s.datavalue)
        s=s.nextvalue
def reverselist(node):
    current=node
    prev=None
    while current!=None:
        next=current.nextvalue
        current.nextvalue=prev
        prev=current
        current=next
    node=prev
    return node
def rearrange(node):
    slow=node
    fast=node.next
    while fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    node1=node
    node2=slow.nextvalue
    slow.nextvalue=None
    node2=reverselist(node2)
    node=Node(0)
    curr=node
    while node1!=None or node2!=None:
        if node1!=None:
            curr.nextvalue=node1
            curr=curr.nextvalue
            node1=node1.nextvalue
        if node2!=None:
            curr.nextvalue=node2
            curr=curr.nextvalue
            node2=node2.nextvalue
    node=node.nextvalue
