class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(idx, i, j, visited):
            if (idx >= length):
                return True
            if (not (i >= 0 and i < n and j >= 0 and j < m)):
                return False
            if (word[idx] == board[i][j] and (i, j) not in visited):
                to_add = set(visited)
                to_add.add((i, j))
                return True and (dfs(idx + 1, i, j - 1, to_add) or 
                                dfs(idx + 1, i, j + 1, to_add) or 
                                dfs(idx + 1, i + 1, j, to_add) or 
                                dfs(idx + 1, i - 1, j, to_add))
            else:
                return False
        n, m = len(board), len(board[0])
        length = len(word)
        for i in range(n):
            for j in range(m):
                visited = set()
                res = dfs(0, i, j, visited)
                if (res):
                    return res
        return False