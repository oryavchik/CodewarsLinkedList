def stringify(node):
    result = []
    while node:
        result.append(str(node.data))
        result.append('->')
        node = node.next
    result.append('None')
    result = ' '.join(result)
    return result
