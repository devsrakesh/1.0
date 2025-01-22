class BTreeNode:
    def __init__(self, t, is_leaf):
        self.t = t  # Minimum degree
        self.keys = []  # Keys in the node
        self.children = []  # Children pointers
        self.is_leaf = is_leaf  # True if the node is a leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)  # Root node
        self.t = t  # Minimum degree

    def search(self, key, node=None):
        """Search for a key in the B-Tree."""
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:
            return node, i  # Key found in the current node
        if node.is_leaf:
            return None  # Key not found
        return self.search(key, node.children[i])  # Search in the appropriate child

    def insert(self, key):
        """Insert a key into the B-Tree."""
        root = self.root
        if len(root.keys) == 2 * self.t - 1:  # If root is full
            new_root = BTreeNode(self.t, False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        """Insert a key into a non-full node."""
        i = len(node.keys) - 1
        if node.is_leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        """Split a full child of a node."""
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(t, child.is_leaf)
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[t:]
        child.keys = child.keys[:t - 1]
        if not child.is_leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]

    def print_tree(self, node=None, level=0):
        """Print the B-Tree for visualization."""
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.is_leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# Create a B-Tree with minimum degree 3
b_tree = BTree(3)

# Insert keys
keys_to_insert = [10, 20, 5, 6, 12, 30, 7, 17]
for key in keys_to_insert:
    b_tree.insert(key)

# Print the B-Tree structure
print("B-Tree Structure After Insertion:")
b_tree.print_tree()

# Search for keys
search_keys = [6, 15, 30]
for key in search_keys:
    result = b_tree.search(key)
    if result:
        node, index = result
        print(f"Key {key} found in node with keys: {node.keys}")
    else:
        print(f"Key {key} not found in the B-Tree.")
