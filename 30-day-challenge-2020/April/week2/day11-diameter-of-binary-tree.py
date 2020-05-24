# Diameter of Binary Tree
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

##############################################################################################
# Complexity Analysis                                                                        #
# Time Complexity: O(N). We visit every node once.                                           #
# Space Complexity: O(N), the size of our implicit call stack during our depth-first search. #
##############################################################################################
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def depth(self, root):
        if not root:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)
        max_depth = max(l, r) + 1
        self.ans = max(l+r, self.ans)
        return max_depth

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.ans = 0
        self.depth(root)
        return self.ans
