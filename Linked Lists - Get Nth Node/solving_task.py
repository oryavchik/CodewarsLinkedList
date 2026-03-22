"""Linked Lists - Get Nth Node"""

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """Function"""
    i = 0
    while node:
        if i == index:
            return node
        node = node.next
        i += 1

    raise ValueError
