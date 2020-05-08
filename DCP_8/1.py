
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def countNumTrees(root):
    count, val = isUniVal(root)
    return count

def isUniVal(root):
    if root is None:
        return 0, True
    count_left, isLeft = isUniVal(root.left)
    count_right, isRight = isUniVal(root.right)
    if isLeft and isRight:
        if root.left is not None and root.data != root.left.data:
            return count_left+count_right, False
        if root.right is not None and root.data != root.right.data:
            return count_left+count_right, False
        return count_left+count_right+1, True
    return count_left+count_right, False

if __name__ == '__main__':
    a = Node(0)
    a.left = Node(1)
    a.right = Node(0)

    a.right.left = Node(1)
    a.right.right = Node(0)

    a.right.left.left = Node(1)
    a.right.left.right = Node(1)

    print(countNumTrees(a))
