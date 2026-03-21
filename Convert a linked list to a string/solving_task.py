"""Convert a linked list to a string"""
def stringify(node):
    """Function"""
    result = []
    while node:
        result.append(str(node.data))
        result.append('->')
        node = node.next
    result.append('None')
    result = ' '.join(result)
    return result
