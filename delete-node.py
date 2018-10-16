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

def deleteDeepest(root,last):
    if root is None:
        return
    rq=[]
    rq.append(root)
    while(len(rq)>0):
        node=rq.pop(0)
        if node.left is not None:
            if node.left.data == last.data:
                node.left = None
            else:
                rq.append(node.left)
        if node.right is not None:
            if node.right.data == last.data:
                node.right = None
            else:
                rq.append(node.right)
    return node

    
def deleteNode(root,dele):
    if root is None:
        return

    q=[]
    q.append(root)

    while(len(q)>0):
        node=q.pop(0)
        if node.data == dele:
            key_node=node

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

        
    last=node
    deleteDeepest(root,last)
    key_node.data = last.data
    



root = Node(1)
root.left = Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

print("level order traveral of binary tree before deletion is:")
printLevelOrder(root)

print("\nlevel order traversal of binary tree after deletion is:")
deleteNode(root,2)
printLevelOrder(root)
