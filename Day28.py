class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    if not root:
        return True
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left))
    return isMirror(root.left, root.right)


from collections import deque
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] != "null":
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


print(isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))            
print(isSymmetric(build_tree([1, 2, 2, "null", 3, "null", 3])))  
print(isSymmetric(build_tree([1])))                             
print(isSymmetric(build_tree([])))                               
print(isSymmetric(build_tree([1, 2, 2, 3, "null", "null", 3])))  
