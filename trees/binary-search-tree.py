class TreeNode(object):
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinaryTree(object):

    def __init__(self, root=None):
        self.root = root

    @classmethod
    def inorder(cls, node):
        if node:
            cls.inorder(node.left)
            print " {}".format(node.key),
            cls.inorder(node.right)

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            current = self.root
            while current:
                if key < current.key:
                    if current.left is None:
                        current.left = TreeNode(key)
                        break
                    else:
                        current = current.left
                elif key > current.key:
                    if current.right is None:
                        current.right = TreeNode(key)
                        break
                    else:
                        current = current.right


if __name__ == "__main__":
    bst = BinaryTree()

    for key in [50, 30, 20, 40, 70, 60, 80]:
        bst.insert(key)

    bst.inorder(bst.root)



