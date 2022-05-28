# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class Node:
    def __init__(self,data):
        self.datavalue=data
        self.nextvalue=next
class linkedlist:
    def __init__(self):
        self.headvalue=None
    def push(self,key):
        newnode=Node(key)
        newnode.nextvalue=self.headvalue
        self.headvalue=newnode
    def print(self):
        d=self.headvalue
        while d!=None:
            print(d.datavalue)
            d=d.nextvalue
def findnum(head1):
    num1=0
    first_ptr=head1
    while first_ptr!=None:
        num1=(num1*10)+first_ptr.datavalue
        first_ptr=first_ptr.nextvalue
    return num1
def reverse(s):
    a=str(s)
    return a[::-1]
    
ll1=linkedlist()
ll2=linkedlist()
ll1.push(3)
ll1.push(4)
ll1.push(2)
ll1.print()
s=findnum(ll1.headvalue)
q=int(reverse(s))
print(q)
ll2.push(4)
ll2.push(6)
ll2.push(5)
ll2.print()
d=findnum(ll2.headvalue)
j=int(reverse(d))
print(d)
a=j+q
print(a)
w=
