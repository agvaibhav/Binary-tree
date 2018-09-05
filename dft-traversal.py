class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

#inorder tree traversal

def inorder(root):

    if root:

        inorder(root.left)

        print(root.val,end=' ')

        inorder(root.right)
   

# postorder tree traversal

def postorder(root):

    if root:

        postorder(root.left)

        postorder(root.right)

        print(root.val,end=' ')

# preorder tree traversal

def preorder(root):

    if root:

        print(root.val,end=' ')

        preorder(root.left)

        preorder(root.right)

        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("preorder traversal is :")
preorder(root)

print("inorder traversal is :")
inorder(root)

print("postorder traversal is :")
postorder(root)
