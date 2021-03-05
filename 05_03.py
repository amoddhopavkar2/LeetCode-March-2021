# Friday, 5th March 2021
# Average of Levels in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = []
        current = [root]

        while current:
            q.append(current)
            current = []

            for node in q:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
                
        values = [[node.val for node in current] for current in q]
        return (sum(level) / len(level) for level in values)
        
