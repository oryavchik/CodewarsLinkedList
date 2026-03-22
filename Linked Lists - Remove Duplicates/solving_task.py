"""Linked Lists - Remove Duplicates"""
class Node(object):
    """class Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """Function removes duplicates"""
    if head is None:
        return None

    now = head

    while now and now.next:
        if now.data == now.next.data:
            now.next = now.next.next
        else:
            now = now.next

    return head
