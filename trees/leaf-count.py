class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @classmethod
    def leaf_count(cls, node):
        if not node:
            return 0

        if node.left is None and node.right is None:
            return 1

        return cls.leaf_count(node.left) \
             + cls.leaf_count(node.right)


if __name__ == "__main__":
    node = TreeNode(1,
               left=TreeNode(2,
                   left=TreeNode(3),
                   right=TreeNode(5)),
               right=TreeNode(4))

    print "Leaf count of tree is: {}".format(TreeNode.leaf_count(node))

