"""Linked Lists - Sorted Insert"""
class Node(object):
    """class Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """Function sorts"""
    new_node = Node(data)

    if head is None or data < head.data:
        new_node.next = head
        return new_node

    num = head

    while num.next and num.next.data < data:
        num = num.next

    new_node.next = num.next
    num.next = new_node

    return head
