class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
            if self.left is None and self.right is None:
                return self.val
            if self.left is None:
                return self.val + "(" + ", " + str(self.right) + ")"
            if self.right is None:
                return self.val + "(" + str(self.left) + ", " + ")"
            return self.val + "(" + str(self.left) + ", " + str(self.right) + ")"

def serialize(root) -> str:
    if not root:
        return "#"
    return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)

def deserialize(data) -> Node:
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(str(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split(','))
    return helper()
### this approach is O(n) because it iterates through each node of the tree a fixed number of timesc
if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    # print(deserialize(serialize(node)))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
