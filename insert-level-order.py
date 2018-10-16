class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return

    queue=[]

    queue.append(root)

    while(len(queue)>0):
        print(queue[0].data, end=' ')
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

def insertLevelOrder(root,ele):
    if root is None:
        return

    q=[]
    q.append(root)
    while(len(q)>0):
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.left is None:
            node.left=Node(ele.data)
            break

        if node.right is not None:
            q.append(node.right)
        if node.right is None:
            node.right=Node(ele.data)
            break

root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.right=Node(5)

print("level order traveral of binary tree before insertion is:")
printLevelOrder(root)

ele=Node(4)
insertLevelOrder(root,ele)
insertLevelOrder(root,Node(6))
print("\nlevel order traversal of binary tree after insertion is:")
printLevelOrder(root)
