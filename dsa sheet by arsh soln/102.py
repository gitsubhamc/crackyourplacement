class Node:
    def __init__(self,datavalue):
        self.datavalue=datavalue
        self.nextvalue=None
def newnode(key):
    temp=Node(key)
    temp.datavalue=key
    temp.nextvalue=None
    return temp
def printlist(node):
    while(node!=None):
        print(node.datavalue)
        node=node.nextvalue
def merge(h1,h2):
    if h1==None:
        return h2
    if h2==None:
        return h1
    if h1.datavalue<h2.datavalue:
        h1.nextvalue=merge(h1.nextvalue,h2)
        return h1
    else:
        h2.nextvalue=merge(h1,h2.nextvalue)
        return h2

head1=newnode(0)
head1.nextvalue=newnode(3)
head1.nextvalue.nextvalue=newnode(5)
head2=newnode(1)
head2.nextvalue=newnode(2)
head2.nextvalue.nextvalue=newnode(8)
f=merge(head1,head2)
printlist(f)