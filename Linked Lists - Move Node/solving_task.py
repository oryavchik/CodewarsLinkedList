"""Move Node"""
class Node(object):
    """class Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """class Context"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """Function which moves node"""
    if source is None:
        raise ValueError

    moved = source
    source = source.next
    moved.next = dest
    dest = moved

    return Context(source, dest)
