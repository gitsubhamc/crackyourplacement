# # Given the head of a singly linked list, return true if it is a palindrome.
# from typing import List


# class Node:
#     def __init__(self,datavalue):
#         self.datavalue=datavalue
#         self.nextvalue=None
# class Linkedlist:
#     def __init__(self):
#         self.headvalue=None
#     def push(self,key):
#         newnode=Node(key)
#         newnode.nextvalue=self.headvalue
#         self.headvalue=newnode
#     def print(self):
#         g=self.headvalue
#         while g!=None:
#             print(g.datavalue)
#             g=g.nextvalue
# def convert_to_number(first):
#     num=0
#     list=[]
#     first_ptr=first.headvalue
#     while first_ptr!=None:
#         num=(num*10)+first_ptr.datavalue
#         first_ptr=first_ptr.nextvalue
#         # list.append(first_ptr.datavalue)
#     return num
# def pallindrone(d):
#     s=str(d)
#     w=s[::-1]
#     return w

# ll=Linkedlist()
# ll.push(2)
# ll.push(3)
# ll.push(4)
# ll.push(3)
# ll.push(2)
# ll.print()
# print("####*")
# f=convert_to_number(ll)
# c=str(f)
# print(f)
# g=pallindrone(f)
# print(g)
# if g==c:
#     print("yes ")
# else:
#     print("noo")

class Node:
    def __init__(self,data):
        self.datavalue=data
        self.nextvalue=None:
def ispallindrome(head):
    stack=[]
    slow=head
    ispalin=True
    while slow!=None:
        stack.append(slow.data)
        slow=slow.nextvalue
    while head!=None:
        i=stack.pop()
        if i==head.datavalue:
            ispalin=True
        else:
            ispalin=False
            break
        head=head.ptr
    return ispalin
    
 