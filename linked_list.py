from typing import List


class ListNode:
    """A node for a singly linked list."""
    def __init__(self, val, next_node=None):
        """Initialize a new node with a given value and optional next_node reference."""
        self.val = val
        self.next = next_node


class LinkedList:
    """A simple implementation of a single linked list data structure."""
    def __init__(self):
        """Initialize an empty linked list with a reference to the head (dummy) node."""
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        """Retrieve the value at a specified index in the linked list."""
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1  # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None:
        """Insert a new node with the given value at the beginning of the linked list."""
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        """Insert a new node with the given value at the end of the linked list."""
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        """Remove the node at the specified index from the linked list."""
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False  # Index out of bounds or list is empty

    def getValues(self) -> List[int]:
        """Retrieve all values in the linked list as a list."""
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
