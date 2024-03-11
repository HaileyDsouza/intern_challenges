class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        final_list = head
        while list1 and list2:
            if list1.val < list2.val:
                final_list.next = list1
                list1 = list1.next
            else:
                final_list.next= list2
                list2 = list2.next
            final_list = final_list.next
        final_list.next = list1 or list2
        return head.next 
"""You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list."""