"""Can you get the loop ?"""

def loop_size(node):
    """Finding loop size"""
    first = node
    next = node.next

    while first != next:
        first = first.next
        next = next.next.next

    loop = 1
    next = next.next

    while first != next:
        loop += 1
        next = next.next

    return loop
