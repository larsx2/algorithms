class TreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @classmethod
    def print_inorder(cls, node):
        if node:
            cls.print_inorder(node.left)
            print " {} ".format(node.data),
            cls.print_inorder(node.right)

    @classmethod
    def print_preorder(cls, node):
        if node:
            print " {} ".format(node.data),
            cls.print_preorder(node.left)
            cls.print_preorder(node.right)

    @classmethod
    def print_postorder(cls, node):
        if node:
            cls.print_postorder(node.left)
            cls.print_postorder(node.right)
            print " {} ".format(node.data),


if __name__ == "__main__":
    print """
          Tree
            1
          /   \\
         2     4
        / \\
       3   5
    """

    root = TreeNode(1,
            left=TreeNode(2,
                left=TreeNode(3),
                right=TreeNode(5)),
            right=TreeNode(4))

    print "Inorder:"
    TreeNode.print_inorder(root)

    print
    print "Preorder:"
    TreeNode.print_preorder(root)

    print
    print "Postorder:"
    TreeNode.print_preorder(root)
