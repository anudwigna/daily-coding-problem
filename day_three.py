

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None:
        return "None"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"

def deserialize(s):
    def deserialize_helper(nodes):
        if nodes[0] == "None":
            nodes.pop(0)
            return None

        val = nodes.pop(0)
        node = Node(val)
        node.left = deserialize_helper(nodes)
        node.right = deserialize_helper(nodes)
        return node

    nodes = s.split(",")
    return deserialize_helper(nodes)



