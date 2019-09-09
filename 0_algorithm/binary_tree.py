# https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/binary_tree

class Node(object):
    def __init__(self,label):
        self.label=label
        self.left=None
        self.right=None

    def __repr__(self):
        return str(self.label)

### build tree
#       A
#      / \
#     B   H
#    / \
#   C   D
#      / \
#     E   F
#    /
#   G
root = Node('A')
root.left = Node('B')
root.right = Node('H')
root.left.left = Node('C')
root.left.right = Node('D')
root.left.right.left = Node('E')
root.left.right.right = Node('F')
root.left.right.left.left = Node('G')

### traverse
# Preorder (A,B,C,D,E,G,F,H)
def preorder(node):
    if node is None: return
    print(node,end=',')
    preorder(node.left)
    preorder(node.right)

# Inorder (C,B,G,E,D,F,A,H)
def inorder(node):
    if node is None: return
    inorder(node.left)
    print(node,end=',')
    inorder(node.right)

# Postorder (C,G,E,F,D,B,H,A)
def postorder(node):
    if node is None: return
    postorder(node.left)
    postorder(node.right)
    print(node,end=',')

print("--- preorder ---")
preorder(root)
print()
print("--- inorder ---")
inorder(root)
print()
print("--- postorder ---")
postorder(root)
