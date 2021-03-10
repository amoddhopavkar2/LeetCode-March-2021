# Tuesday, 9th March 2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            tmp = root
            output = TreeNode(v)
            output.left = tmp
            return output
        queue = [(root,1)]
        while queue:
            vertex,level = queue.pop(0)
            if level == d:
                return root
            if level == d - 1:
                    tmp = vertex.left
                    vertex.left = TreeNode(v)
                    vertex.left.left = tmp
                    tmp = vertex.right
                    vertex.right = TreeNode(v)
                    vertex.right.right = tmp
            if vertex.left:
                queue.append((vertex.left,level+1))
            if vertex.right:
                queue.append((vertex.right,level+1))