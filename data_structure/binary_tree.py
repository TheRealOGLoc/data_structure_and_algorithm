#in order traversal:
#In this traversal method, the left subtree is visited first, then the root and later the right sub-tree.
#     2
#   /   \
#  1     3
  
#pre order traversal:
#in this traversal method, the root node is visited first, then the left subtree and finally right subtree.
#     1
#   /   \
#  2     3

#post order traversal:
#in this traversal method, we first traverse the left subtree, then the right subtree and finally the root node.
#     3
#   /   \
#  1     2

class BinarySearchTreeNode:  
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data: #binary search tree can not have same value
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self, root):
        result = []
        if root:
            result += self.in_order_traversal(root.left) # concatenate two list together
            result.append(root.data)
            result += self.in_order_traversal(root.right)
        return result

    def pre_order_traversal(self, root):
        result = []
        if root:
            result.append(root.data)
            result += self.pre_order_traversal(root.left)
            result += self.pre_order_traversal(root.right)
        return result
    
    def post_order_traversal(self, root):
        result =[]
        if root:
            result += self.post_order_traversal(root.left)
            result += self.post_order_traversal(root.right)
            result.append(root.data)
        return result
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
def create_binary_tree():
    root = BinarySearchTreeNode(27)
    root.add_child(14)
    root.add_child(35)
    root.add_child(10)
    root.add_child(19)
    root.add_child(31)
    root.add_child(42)
    print(root.in_order_traversal(root))

if __name__ == "__main__":
    create_binary_tree()

