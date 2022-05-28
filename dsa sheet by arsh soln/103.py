
from ast import If


class Node:
    def __init__(self,datavalue):
        self.datavalue=datavalue
        self.nextvalue=None
class Linkedlist():
    def __init__(self):
        self.headvalue=None
    def print(self):
        d=self.headvalue
        while d!=None:
            print(d.datavalue)
            d=d.nextvalue
    def push(self,key):
        newnode=Node(key)
        newnode.nextvalue=self.headvalue
        self.headvalue=newnode
def multiplytwolist(head1,head2):
        first_ptr=head1.headvalue
        second_ptr=head2.headvalue
        num1=0
        num2=0
        while first_ptr!=None or second_ptr!=None:
            if first_ptr!=None:
                num1=(num1*10)+first_ptr.datavalue
                first_ptr=first_ptr.nextvalue
            if second_ptr!=None:
                num2=(num2*10)+second_ptr.datavalue
                second_ptr=second_ptr.nextvalue

        return num1*num2
if __name__=='__main__':
    ll1=Linkedlist()
    ll2=Linkedlist()
    ll1.push(2)
    ll1.push(3)
    ll1.push(4)
    ll2.push(5)
    ll2.push(6)
    ll2.push(7)
    result=multiplytwolist(ll1,ll2)
    print(result)



