class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None
class LinkedList:
    def __init__(self):
        self.headvalue=None
    def convert_binary_to_integer(self,head):
        res=0
        while head :
            res=(res<<1)+head.datavalue
            head=head.nextvalue
        return res
ll=LinkedList()
ll.headvalue=Node(1)
ll.headvalue.nextvalue=Node(1)
ll.headvalue.nextvalue.nextvalue=Node(1)
ll.headvalue.nextvalue.nextvalue.nextvalue=Node(1)
print(ll.convert_binary_to_integer(ll.headvalue))
