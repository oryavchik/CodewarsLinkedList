"""Linked Lists - Push & BuildOneTwoThree"""
class Node:
    """preloaded Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """Function push"""
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """Function building"""
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
