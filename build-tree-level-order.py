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

def insertLevelOrder(arr,root,i):

    if i<len(arr):
        root=Node(arr[i])

        root.left = insertLevelOrder(arr,root.left,2*i+1)

        root.right= insertLevelOrder(arr,root.right,2*i+2)

    return root
    


arr=[1,2,3,4,5,6,7,8,9]
root=Node(arr[0])
tree=insertLevelOrder(arr,root,0)
print("level order traveral of binary tree after insertion is:")
printLevelOrder(tree)

