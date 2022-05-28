class Node:
    def __init__(self,data):
        self.datavalue=data
        self.nextvalue=None
        self.child=None
class Linkedlist:
    def __init__(self):
        self.headvalue=None
    def push(self,key):
        newnode=Node(key)
        newnode.nextvalue=self.headvalue
        self.headvalue=newnode
    def display(self):
        a=self.headvalue
        while a!=None:
            print(a.datavalue)
            a=a.nextvalue
    def flatten(self):
        if not self.headvalue:
            return
        temp=self.headvalue
        while temp.nextvalue!=None:
            temp=temp.nextvalue
        currentnode=self.headvalue
        while currentnode!=temp:
            if currentnode.child:
                temp.next=currentnode.child
                tmp=currentnode.child
                while tmp.next():
                    tmp=tmp.nextvalue
                temp=tmp
        currentnode=currentnode.nextvalue

