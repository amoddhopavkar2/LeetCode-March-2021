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
        