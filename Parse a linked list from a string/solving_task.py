"""Parse a linked list from a string"""
from preloaded import Node

def linked_list_from_string(string):
    """Function"""
    if string == 'null':
        return None

    text = string.split('->')
    text = text[:-1]

    node = None

    for i in range(len(text)-1, -1, -1):
        val = text[i].strip()
        node = Node(int(val), node)

    return node
