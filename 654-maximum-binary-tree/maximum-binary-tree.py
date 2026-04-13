# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def constructMaximumBinaryTree(self, nums):

        def build(arr):
            if not arr:
                return None

            # find max value and index
            max_val = max(arr)
            idx = arr.index(max_val)

            # create root
            root = TreeNode(max_val)

            # build left and right subtree
            root.left = build(arr[:idx])
            root.right = build(arr[idx+1:])

            return root

        return build(nums)