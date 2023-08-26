class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root) -> str:
    if not root.val:
        return " "
    strval = str(root.val)
    return strval + "," + serialize(root.left) + "," + serialize(root.right)
    serialize(root.left)
    serialize(root.right)
def deserialize(root) -> str:
    '''
    The recursion for serialize is not correct so it is very difficult for me to come up with the recursion for deserialize.
    '''




if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))