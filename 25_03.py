# Thursday, 25th March 2021
# Pacific Atlantic Water Flow

class Solution:
    
    def isValid(self, i, j, rows, cols):
        return 0 <= i < rows and 0 <= j < cols    

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        pacific, atlantic, ans = set(), set(), []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(matrix, i, j, ocean, prev):
            if not self.isValid(i, j, rows, cols) or ((i, j) in ocean):
                return
            if prev > matrix[i][j]:
                return
            ocean.add((i, j))
            for x, y in directions:
                dfs(matrix, i + x, j + y, ocean, matrix[i][j])
            
        for k in range(rows):
            dfs(matrix, k, 0, pacific, matrix[k][0])
            dfs(matrix, k, cols - 1, atlantic, matrix[k][cols - 1])
        
        for k in range(cols):
            dfs(matrix, 0, k, pacific, matrix[0][k])
            dfs(matrix, rows - 1, k, atlantic, matrix[rows - 1][k])
        
        return list(pacific.intersection(atlantic))
