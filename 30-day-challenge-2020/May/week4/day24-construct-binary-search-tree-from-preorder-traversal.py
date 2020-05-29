# Construct Binary Search Tree from Preorder Traversal
# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Example 1:
# Input: [8, 5, 1, 7, 10, 12]
# Output: [8, 5, 10, 1, 7, null, 12]

# Constraints:
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10 ^ 8
# The values of preorder are distinct.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, node, val):

        if not node:
            node = TreeNode(val)
        elif val < node.val:
            node.left = self.buildTree(node.left, val)
        else:
            node.right = self.buildTree(node.right, val)

        return node

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = None
        for val in preorder:
            root = self.buildTree(root, val)

        return root
