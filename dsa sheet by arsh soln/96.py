class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None
class Linkedlist:
    def __init__(self):
        self.headvalue=None
    def print(self):
        ptr=self.headvalue
        while ptr is not None:
            d=ptr.datavalue
            print(d)
            ptr=ptr.nextvalue
    def insertatbeg(self,newdata):
        node=Node(newdata)
        node.nextvalue=self.headvalue
        self.headvalue=node
    def middleelement(self):
        slow=fast=self.headvalue
        while fast and fast.nextvalue:
            slow=slow.nextvalue
            fast=fast.nextvalue.nextvalue
        return slow.datavalue

ss=Linkedlist()
ss.headvalue=Node("joni")
ss.insertatbeg("boni")
ss.insertatbeg("subham")
ss.insertatbeg("puja")
ss.insertatbeg("roni")
print("the middle element is  "+ss.middleelement())
ss.print()