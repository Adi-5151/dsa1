class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def MergeTwoList(list1, list2):
    dummy = ListNode(-1)
    current = dummy
    while list1 and list2:
         if list1.val < list2.val:
             current.next = list1
             list1 = list1.next
         else:
             current.next = list2
             list2 = list2.next
         current =  current.next
    current.next =  list1 or list2
    return dummy.next



A=ListNode(10)
A.next=ListNode(20)

A.next.next=ListNode(30)

B=ListNode(40)
B.next=ListNode(50)
B.next.next=ListNode(60)

C=MergeTwoList(A,B)
print(C)





