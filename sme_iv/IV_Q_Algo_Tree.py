
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: Write a function that checks if a given binary tree is a valid binary search tree. 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class TreeNode:
    def __init__(self, value=0, left=None, right=None): 
        self.value = value 
        self.left = left 
        self.right = right 

def is_valid_bst(root, left=None, right=None): 
    if not root:
        return True

    if left and root.value <= left.value:
        return False
    if right and root.value >= right.value:
        return False

    return is_valid_bst(root.left, left, root) and is_valid_bst(root.right, root, right)
# Valid BST
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(is_valid_bst(root))  # Output: True

# Invalid BST (right child 1 is < root 2)
bad_root = TreeNode(2, TreeNode(1), TreeNode(1))
print(is_valid_bst(bad_root))  # Output: False


