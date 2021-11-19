"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    if(root.left):
        postOrder(root.left) 
    if(root.right):
        postOrder(root.right)
        
    print(str(root.info)+ " ", end="")