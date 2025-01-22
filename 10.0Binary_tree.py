class Node:
    """Class representing a node in the binary search tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class representing the binary search tree."""
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        """Insert a key into the binary search tree."""
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        """Search for a key in the binary search tree."""
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, root, key):
        """Delete a key from the binary search tree."""
        if root is None:
            return root

        # Traverse the tree to find the key
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def find_min(self, root):
        """Find the node with the minimum key."""
        current = root
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        """Perform an inorder traversal of the tree."""
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)


# Example Usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    root = None

    # a) Construct a BST with some elements
    elements = [50, 30, 70, 20, 40, 60, 80]
    for elem in elements:
        root = bst.insert(root, elem)

    print("Inorder Traversal of the Binary Search Tree:")
    bst.inorder_traversal(root)
    print("\n")

    # b) Search for a key in the BST
    key_to_search = 40
    result = bst.search(root, key_to_search)
    if result:
        print(f"Element {key_to_search} found in the BST.")
    else:
        print(f"Element {key_to_search} not found in the BST.")

    # c) Delete an element from the BST
    key_to_delete = 50
    print(f"\nDeleting element {key_to_delete} from the BST...")
    root = bst.delete(root, key_to_delete)

    print("Inorder Traversal after Deletion:")
    bst.inorder_traversal(root)
    print()
