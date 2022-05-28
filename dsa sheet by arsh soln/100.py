class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None
class LinkedList:
    def __init__(self):
        self.headvalue=(None)
    def sorting_of_linked_list(self):
        count=[0,0,0]
        ptr=self.headvalue
        while ptr != None:
            count[ptr.datavalue]+=1
            ptr=ptr.nextvalue
        i=0
        ptr=self.headvalue
        while ptr!= None:
            if count[i]==0:
                i+=1
            else:
                ptr.datavalue=i
                count[i]-=1
                ptr=ptr.nextvalue
    def print(self):
        printval=self.headvalue
        while printval is not None:
            print(printval.datavalue)
            printval=printval.nextvalue      

ll=LinkedList()
ll.headvalue=Node(1)
ll.headvalue.nextvalue=Node(2)
ll.headvalue.nextvalue.nextvalue=Node(0)
ll.headvalue.nextvalue.nextvalue.nextvalue=Node(0)
ll.sorting_of_linked_list()
ll.print()