class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(string):
    if string == 'null':
        return None

    text = string.split('->')
    text = text[:-1]

    node = None

    for i in range(len(text)-1, -1, -1):
        val = text[i].strip()
        node = Node(int(val), node)

    return node
