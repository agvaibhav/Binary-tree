class et:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def isOperator(c):
    if (c=="+" or c=="-" or c=="*" or c=="/" or c=="^"):
        return True
    else:
        return False

def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.value,end=' ')
        inorder(t.right)

def buildTree(postfix):
    stack=[]

    for char in postfix:
        if not isOperator(char):
            t=et(char)
            stack.append(t)

        else:
            t=et(char)
            t1=stack.pop()
            t2=stack.pop()

            t.right=t1
            t.left=t2

            stack.append(t)

    t=stack.pop()

    return t


postfix = "ab+ef*g*-"
r=buildTree(postfix)
print("infix expression is:")
inorder(r)
