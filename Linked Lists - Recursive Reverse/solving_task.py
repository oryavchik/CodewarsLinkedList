"""Linked Lists - Recursive Reverse"""
class Node(object):
    """class Node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """Function reverses"""
    if head is None or head.next is None:
        return head

    new = reverse(head.next)
    head.next.next = head
    head.next = None
    return new
