class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        preorder_recursive(node.left, result)
        preorder_recursive(node.right, result)
    return result


def inorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_recursive(node.left, result)
        result.append(node.value)
        inorder_recursive(node.right, result)
    return result


def postorder_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        postorder_recursive(node.left, result)
        postorder_recursive(node.right, result)
        result.append(node.value)
    return result


def preorder_iterative(root):
    if not root:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def inorder_iterative(root):
    stack, result = [], []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


def postorder_iterative(root):
    if not root:
        return []
    stack1, stack2, result = [root], [], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        result.append(stack2.pop().value)
    return result


# Constructing a binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# Recursive Traversals
print("Recursive Preorder:", preorder_recursive(root))
print("Recursive Inorder:", inorder_recursive(root))
print("Recursive Postorder:", postorder_recursive(root))

# Iterative Traversals
print("Iterative Preorder:", preorder_iterative(root))
print("Iterative Inorder:", inorder_iterative(root))
print("Iterative Postorder:", postorder_iterative(root))
