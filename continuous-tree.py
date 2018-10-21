class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =  None

def treeContinuous(root):

    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is None:
        return(abs(root.data - root.right.data)==1 and treeContinuous(root.right))

    if root.right is None:
        return(abs(root.data - root.left.data)==1 and treeContinuous(root.left))

    return (abs(root.data - root.right.data)==1 and abs(root.data - root.left.data)==1 and treeContinuous(root.left) and treeContinuous(root.right))


root = Node(1)
root.left= Node(2)
root.left.left=Node(3)
root.left.right = Node(3)
root.right = Node(2)
root.right.right = Node(3)

if treeContinuous(root):
    print("the given tree is continuous")

else:
    print("the given tree is not continuous")
