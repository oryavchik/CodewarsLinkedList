"""Swap Node Pairs In Linked List"""
class Node:
    """class Node"""
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """Function swaps pairs"""
    if head is None or head.next is None:
        return head

    first = head
    second = head.next

    first.next = swap_pairs(second.next)
    second.next = first

    return second
