class Node:
    def __init__(self, data):
        self.datavalue=data
        self.nextvalue=None
        self.random=None
def Clone(root):
    current=root
    while current!=None:
        new=Node(current.datavalue)
        new.nextvalue=current.nextvalue
        current.nextvalue=new
        current=current.nextvalue.nextvalue
    current=root
    #adjusting the random pointer
    while current!=None:
        current.nextvalue.random=current.random.nextvalue
        current=current.nextvalue.nextvalue
    #detaching original and duplicate
    current=root
    dup_root=root.nextvalue
    while current.next!=None:
        tmp=current.nextvalue
        current.nextvalue=current.nextvalue.nextvalue
        current=tmp
    return dup_root
def print(root):
    s=root
    while s!=None:
        # print("data is=",s.datavalue,",random is= ",s.random.datavalue)
        print('Data =', s.datavalue, ', Random =', s.random.datavalue)
        s=s.nextvalue

originlll=Node(1)
originlll.nextvalue=Node(2)
originlll.nextvalue.nextvalue=Node(4)
originlll.nextvalue.nextvalue.nextvalue=Node(3)
#assigning the random
originlll.random=originlll.nextvalue.nextvalue
originlll.nextvalue.random=originlll
originlll.nextvalue.nextvalue.random=originlll.nextvalue
originlll.nextvalue.nextvalue.nextvalue.random=originlll.nextvalue.nextvalue
print(originlll)

