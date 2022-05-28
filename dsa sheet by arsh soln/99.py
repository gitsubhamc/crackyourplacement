class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None
class LinkedList:
    def __init__(self):
        self.headvalue=None
    def delete_particular(self,key):
        temp=self.headvalue
    #if the node to be deleted is the first node
        if temp is not None:
            if (temp.datavalue==key):
                self.nextvalue=temp.nextvalue
                temp=None
                return
    #if the node is not the first node
        while temp is not None:
            if temp.datavalue==key:
                break
            prev=temp
            temp=temp.nextvalue
            if temp==None:
                return
            prev.nextvalue=temp.nextvalue
            temp=None
    def print(self):
        printval=self.headvalue
        while printval is not None:
            s=printval.datavalue
            print(s)
            printval=printval.nextvalue
    def remove_duplicates(self):
        r=self.headvalue
        while r.nextvalue is not None:
            if r.datavalue==r.nextvalue.datavalue:
                new=r.nextvalue.nextvalue
                r.nextvalue=new
            else:
                r=r.nextvalue
        return self.headvalue


ll=LinkedList()
ll.headvalue=Node(1)
ll.headvalue.nextvalue=Node(2)
ll.headvalue.nextvalue.nextvalue=Node(2)
ll.remove_duplicates()
ll.print()






