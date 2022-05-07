class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None
class linkedlist:
    def __init__(self):
        self.headvalue=None
    def print(self):
        printval=self.headvalue
        while printval is not None:
            print(printval.datavalue)
            printval=printval.nextvalue
    def insertatbeg(self,newdata):
        newnode=Node(newdata)
        newnode.nextvalue=self.headvalue
        self.headvalue=newnode
    def insertatend(self,newdata):
        Newnode=Node(newdata)
        if self.headvalue is None:
            self.headvalue=Newnode
            return
        laste=self.headvalue
        while (laste.nextvalue):
            laste=laste.nextvalue
        laste.nextvalue=Newnode
    def check_whether_a_cycle(self):
        s=set()
        d=self.headvalue
        while d:
            if d in s:
                return True
            s.add(d)
            d=d.nextvalue
        return False

Linkedlist=linkedlist()
Linkedlist.headvalue=Node("1")
Linkedlist.insertatend("2")
Linkedlist.insertatend("3")
Linkedlist.insertatend("4")
Linkedlist.insertatend("5")
#creating a loop for testing
Linkedlist.headvalue.nextvalue.nextvalue.nextvalue.nextvalue.nextvalue=Linkedlist.headvalue
if (Linkedlist.check_whether_a_cycle()):
    print("loop found")
else:
    print("no loop")