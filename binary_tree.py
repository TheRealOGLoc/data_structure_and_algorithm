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
        
        if data < self.left:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    