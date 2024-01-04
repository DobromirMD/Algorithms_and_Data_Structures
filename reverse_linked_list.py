class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"value: {self.value}, next: {self.next}"
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return head

        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head
