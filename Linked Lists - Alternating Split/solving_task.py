"""Linked Lists - Alternating Split"""

class Node(object):
    """class Node"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """class Context"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """Alternating Split"""
    if head is None or head.next is None:
        raise ValueError

    first_head = head
    second_head = head.next

    first = first_head
    second = second_head

    while second and second.next:
        first.next = second.next
        first = first.next
        second.next = first.next
        second = second.next

    first.next = None

    return Context(first_head, second_head)
