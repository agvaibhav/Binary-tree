class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(inorder, preorder, instart, inend):

    if instart>inend:
        return None

    tnode = Node(preorder[buildTree.preindex])
    buildTree.preindex += 1

    if instart == inend:
        return tnode

    index = search(inorder, instart, inend, tnode.data)

    tnode.left = buildTree(inorder, preorder, instart, index-1)
    tnode.right = buildTree(inorder, preorder, index+1, inend)

    return tnode



def search(arr, start, end, value):
        for i in range(start, end+1):
            if arr[i]==value:
                return i

def inorder(root):
        if root is None:
            return

        inorder(root.left)
        print(root.data,end = ' ')
        inorder(root.right)

        
inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

buildTree.preindex = 0

root = buildTree(inOrder, preOrder, 0 , len(inOrder)-1)

print("inorder traversal of constructed tree is :")
inorder(root)
