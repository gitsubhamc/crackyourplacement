class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None
class LinkedList:
    def __init__(self):
        self.headvalue=None
    def delete_elements(self,key):
        ptr=self.headvalue
        prev=None
        while (ptr!=None and ptr.datavalue==key):
            self.headvalue=ptr.nextvalue
            ptr=self.headvalue
        while ptr!=None:
            while (ptr!=None and ptr.datavalue!=key):
                prev=ptr
                ptr=ptr.nextvalue
            if ptr==None:
                return self.headvalue
            prev.nextvalue=ptr.nextvalue
            ptr=prev.nextvalue
        return self.headvalue
    def print(self):
        printval=self.headvalue
        while printval is not None:
            s=printval.datavalue
            print(s)
            printval=printval.nextvalue

ll=LinkedList()
ll.headvalue=Node(0)
ll.headvalue.nextvalue=Node(1)
ll.headvalue.nextvalue.nextvalue=Node(2)
ll.headvalue.nextvalue.nextvalue.nextvalue=Node(3)
ll.headvalue.nextvalue.nextvalue.nextvalue.nextvalue=Node(3)
ll.delete_elements(3)
ll.print()



