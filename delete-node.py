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

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end = ' ')
    inorder(root.right)

    
def deleteDeepest(root,last):
    if root is None:
        return
    rq=[]
    rq.append(root)
    while(len(rq)>0):
        node=rq.pop(0)
        if node == last:
            node = None
            return
        if node.right:
            if node.right == last:
                node.right = None
                return
            else:
                rq.append(node.right)

        if node.left:
            if node.left == last:
                node.left = None
                return
            else:
                rq.append(node.left)
        

    
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
    


if __name__=='__main__':
    root = Node(10) 
    root.left = Node(11) 
    root.left.left = Node(7) 
    root.left.right = Node(12) 
    root.right = Node(9) 
    root.right.left = Node(15) 
    root.right.right = Node(8) 
    print("The tree before the deletion:") 
    inorder(root)
    print()
    printLevelOrder(root)
    key = 11
    deleteNode(root, key) 
    print() 
    print("The tree after the deletion;") 
    inorder(root)
    print()
    printLevelOrder(root)
