class Node:
    def __init__(self,data):
        self.datavalue=data
        self.nextvalue=None
        self.prevvalue=None
class deque:
    def __init__(self):
        self.headvalue=None
        self.tailvalue=None
    def isempty(self):
        if self.headvalue==None:
            return True
        return False
    def size(self):
        if not self.isempty():
            temp=self.headvalue
            len=0
            while temp!=None:
                len+=1
                temp=temp.nextvalue
            return len
        return 0
    def insertatbeg(self,value):
        newnode=Node(value)
        if self.headvalue==None:
            self.headvalue=self.tailvalue=newnode
            newnode.nextvalue=newnode.prevvalue=None
        else:
            self.headvalue.prevvalue=newnode
            newnode.nextvalue=self.headvalue
            newnode.prevvalue=None
            self.headvalue=newnode
    def insertatend(self,value):
        newnode=Node(value)
        if self.headvalue==None:
            self.headvalue=self.tailvalue=newnode
            newnode.nextvalue=newnode.prevvalue=None
        else:
            self.tailvalue.nextvalue=newnode
            newnode.prevvalue=self.headvalue
            newnode.nextvalue=None
            self.tailvalue=newnode
    def remove_first(self):
        if not self.isempty():
            temp=self.headvalue
            self.headvalue=self.headvalue.nextvalue
            if self.headvalue:
                self.headvalue.prevvalue=None
#no need pythns garbage collector will auto do it delete(temp)
            if self.headvalue==None:
                self.tailvalue=None
                return
        else:
            print("list is empty")
    def remove_last(self):
        if not self.isempty():
            temp=self.tailvalue
            self.tailvalue=self.tailvalue.prevvalue
            if self.tailvalue:
                self.tailvalue.nextvalue=None
                #delete(temp)
            if self.tailvalue==None:
                self.headvalue=None
                return
        else:
            print("list is empty")
    def display(self):
        if not self.isempty():
            temp=self.headvalue
            while temp!=None:
                print(temp.datavalue)
                temp=temp.nextvalue
            return
        else:
            print("list empty")
#till upto this these are the functions of dequeue
#now applying stack
    def push(self,datavalue):
        self.insertatend(datavalue)

    def pop(self):
        self.remove_last()

#now applying queue
    def enqueue(self,datavalue):
        self.insertatend(datavalue)

    def dequeue(self):
        self.remove_first()

stack=deque()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("*********************************************")

queue=deque()
queue.enqueue(1)
queue.enqueue(2)
queue.display()





