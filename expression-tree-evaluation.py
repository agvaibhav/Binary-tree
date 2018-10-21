class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def evaluateET(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return int(root.data)

    left_sum = evaluateET(root.left)
    
    right_sum = evaluateET(root.right)

    if root.data == "+":
        return left_sum + right_sum

    elif root.data == "-":
        return left_sum - right_sum

    elif root.data == "*":
        return left_sum * right_sum

    elif root.data == "/":
        return left_sum / right_sum

    else:
        return("operation is unknown")


root = node('+') 
root.left = node('*') 
root.left.left = node('5') 
root.left.right = node('4') 
root.right = node('-') 
root.right.left = node('100') 
root.right.right = node('20') 
print(evaluateET(root) )
  
root = None
   
root = node('+') 
root.left = node('*') 
root.left.left = node('5') 
root.left.right = node('4') 
root.right = node('-') 
root.right.left = node('100') 
root.right.right = node('/') 
root.right.right.left = node('20') 
root.right.right.right = node('2') 
print(evaluateET(root)) 
