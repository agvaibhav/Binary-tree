class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    s=[]
    q=[]
    q.append(root)

    while(len(q)>0):
        root=q.pop(0)
        s.append(root)

        if(root.right):
            q.append(root.right)

        if root.left:
            q.append(root.left)


    while(len(s)>0):
        root=s.pop()
        print(root.data,end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("reverse level order traversal of binary tree is:")
reverseLevelOrder(root)
