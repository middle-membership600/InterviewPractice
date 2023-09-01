class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
count = 0
def ucount(root : Node) -> bool:
    global count
    # empty tree
    if not root:
        return True

    elif root.left and root.right:
        if (ucount(root.left) and ucount(root.right)) and (root.left.val == root.val and root.right.val == root.val):
            count += 1
            return True
    elif root.left and not root.right:
        if (ucount(root.left) and ucount(root.right)) and (root.left.val == root.val):
            count += 1
            return True
    elif root.right and not root.left:
        if (ucount(root.right) and ucount(root.left)) and (root.right.val == root.val):
            count += 1
            return True
    elif not root.left and not root.right:
        count +=1
        return True
    else:
        return False

# Unfortunately this has O(2^n) complexity because in the worst case each node makes two recursive calls to the function.
# To fix this we need memoization

if __name__ == "__main__":
    root = Node(1,Node(1), Node(0,Node(1,Node(1),Node(1)),Node(0)))
    # root = Node(1)
    ucount(root)
    print(count)