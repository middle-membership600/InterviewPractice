class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root):
    # Base case
    if not root:
        return 0, True

    left_count, is_left_unival = count_unival_subtrees(root.left)
    right_count, is_right_unival = count_unival_subtrees(root.right)

    # Initialize total_count with sum of unival subtrees from left and right
    total_count = left_count + right_count

    # Check if current node forms a unival subtree
    if is_left_unival and is_right_unival:
        if (root.left and root.left.val == root.val or not root.left) and \
           (root.right and root.right.val == root.val or not root.right):
            total_count += 1
            return total_count, True
    
    return total_count, False

if __name__ == "__main__":
    root = Node(1, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    count, _ = count_unival_subtrees(root)
    print(count)  # Output: 5
